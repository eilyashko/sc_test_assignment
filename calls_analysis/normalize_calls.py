"""
Normalize calls.csv to one row per Call ID.

Rules implemented (per user spec; aligned with output):
- Prefer existing numeric/flag columns. 'Talking' text is parsed only for
  total_IVR, total_queue_unanswered, and to augment outbound total_talk.
- 'Ringing' text is used only to detect zero-ring IVR legs; no durations are
  derived from it.
- Per Call ID output columns (in order):
  * call_id — from "Call ID"
  * call_start_time — earliest "Call Time" (ISO with seconds)
  * outside_working_hours — 1 if before 08:00 or at/after 20:00, else 0
  * Direction — "Inbound" if any inbound-like leg; else "Outbound"
  * Outbound_call_answered — 1 if Outbound and any Status=="Answered"
  * Inbound_call_answered — 1 if first_agent_answer_time exists, else 0
  * first_agent_answer_time — first 'Inbound'+'Answered' after last 'Inbound Queue'+'Waiting'; else empty
  * total_IVR — sum 'Talking' seconds for zero-ring Inbound Answered legs before queue
  * total_queue_unanswered — sum 'Talking' seconds for 'Inbound Queue'+'Unanswered'
  * total_queue_wait — sum "Wait Time in Queue" excluding 'Inbound Queue'+'Unanswered' rows
  * total_ring — sum "Ring time"
  * total_talk — sum "Talk Time" (+ 'Talking' text when Outbound)
  * total_call_duration (excl. IVR) — numeric total + total_queue_unanswered (+ outbound ring and talk)
  * total_call_duration (incl. IVR) — excl + total_IVR
  * cost_sum — sum "Cost"
  * sla_breach — max "SLA breach"
  * abandon — max "Abandon"
  * abandon_within_10s — max "Abandon (within 10s)"
  * environment — last non-empty "Environment (from Extension)"
  * start_day — date of call_start_time (YYYY-MM-DD)
  * week — first non-null "week" by time
  * start_hour — hour of call_start_time
  * month — month of call_start_time
  * year — year of call_start_time

Additional aggregation specifics:
  * For Outbound calls, include numeric ring time and 'Talking' text in both
    total call duration fields (excl./incl. IVR).
  * To avoid duplication, when any 'Inbound Queue' + 'Unanswered' rows exist,
    their 'Wait Time in Queue' is excluded from 'total_queue_wait'.
  * Queue metrics order in output: total_IVR, total_queue_unanswered, total_queue_wait.

CLI:
  python normalize_calls.py \
    --input "/Users/evgeniiliashko/repos/scalable_capital/original_data/calls.csv" \
    --output /Users/evgeniiliashko/repos/scalable_capital/calls_normalized.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd


# Column names (as in CSV)
COL_CALL_ID = "Call ID"
COL_CALL_TIME = "Call Time"
COL_DIRECTION = "Direction"
COL_STATUS = "Status"
COL_WAIT_QUEUE = "Wait Time in Queue"
COL_TOTAL_WAIT_Q_RING = "Total Waiting Time (queue+ring)"
COL_TALK_TIME = "Talk Time"
COL_TOTAL_CALL_EXCL_IVR = "Total Call Duration (excl IVR)"
COL_COST = "Cost"
COL_SLA_BREACH = "SLA breach"
COL_ABANDON = "Abandon"
COL_ABANDON_10S = "Abandon (within 10s)"
COL_ENV = "Environment (from Extension)"
COL_WEEK = "week"
COL_RING_TIME = "Ring time"
COL_RINGING_TEXT = "Ringing"
COL_TALKING_TEXT = "Talking"


def robust_parse_datetime(series: pd.Series) -> pd.Series:
    """Parse datetime trying month-first first, then day-first; pick the better parse.

    Many rows look like '8/4/25 11:56' and the dataset's 'week' indicates August 2025,
    so month-first (m/d/yy) is plausible. We still try both and keep the one
    yielding more non-nulls.
    """
    s = series.astype(str)
    dt_m_first = pd.to_datetime(s, errors="coerce", dayfirst=False, infer_datetime_format=True)
    dt_d_first = pd.to_datetime(s, errors="coerce", dayfirst=True, infer_datetime_format=True)
    if dt_m_first.notna().sum() >= dt_d_first.notna().sum():
        return dt_m_first
    return dt_d_first


def to_num(s: pd.Series) -> pd.Series:
    return pd.to_numeric(s, errors="coerce")


def last_non_empty(series: pd.Series) -> Optional[str]:
    if series is None or series.empty:
        return None
    if series.dtype != object:
        series = series.astype(str)
    vals = [v for v in series if pd.notna(v) and str(v).strip() != ""]
    return vals[-1] if vals else None


def first_non_null(series: pd.Series):
    for v in series:
        if pd.notna(v):
            return v
    return None


def find_first_human_answer_time(g: pd.DataFrame, time_col: str) -> Optional[pd.Timestamp]:
    """Given a group sorted by time_col, find first 'Inbound'+'Answered' after last 'Inbound Queue'+'Waiting'.

    Uses normalized Direction/Status values (stripped, collapsed spaces, lowercase) for robustness.
    """
    dir_norm = (
        g[COL_DIRECTION].astype(str).str.replace(r"\s+", " ", regex=True).str.strip().str.lower()
        if COL_DIRECTION in g
        else pd.Series(["" for _ in range(len(g))], index=g.index)
    )
    status_norm = (
        g[COL_STATUS].astype(str).str.replace(r"\s+", " ", regex=True).str.strip().str.lower()
        if COL_STATUS in g
        else pd.Series(["" for _ in range(len(g))], index=g.index)
    )
    mask_queue_wait = (dir_norm == "inbound queue") & (status_norm == "waiting")
    if not mask_queue_wait.any():
        return None
    # last index of queue waiting
    last_pos = np.where(mask_queue_wait.values)[0][-1]
    if last_pos >= len(g) - 1:
        return None
    remainder = g.iloc[last_pos + 1 :]
    dir_norm_rem = dir_norm.iloc[last_pos + 1 :]
    status_norm_rem = status_norm.iloc[last_pos + 1 :]
    mask_answer = (dir_norm_rem == "inbound") & (status_norm_rem == "answered")
    if not mask_answer.any():
        return None
    first_row = remainder.loc[mask_answer].iloc[0]
    return first_row[time_col]


def _parse_hms_to_seconds(value: object) -> Optional[int]:
    if pd.isna(value):
        return None
    try:
        s = str(value).strip()
        parts = s.split(":")
        if len(parts) == 3:
            h, m, sec = [int(float(p)) for p in parts]
            return h * 3600 + m * 60 + sec
        if len(parts) == 2:
            m, sec = [int(float(p)) for p in parts]
            return m * 60 + sec
        return int(float(s))
    except Exception:
        return None


def _ringing_is_zero(value: object) -> bool:
    if pd.isna(value):
        return False
    s = str(value).strip()
    if s in {"0:00:00", "00:00:00", "0:0:0"}:
        return True
    secs = _parse_hms_to_seconds(s)
    return bool(secs == 0)


def normalize_calls(df: pd.DataFrame) -> pd.DataFrame:
    # Parse time for ordering and derived fields
    df = df.copy()
    dt = robust_parse_datetime(df[COL_CALL_TIME])
    df["__call_time_dt"] = dt

    # Ensure numeric/flags are numeric
    for c in [
        COL_WAIT_QUEUE,
        COL_TOTAL_WAIT_Q_RING,
        COL_TALK_TIME,
        COL_TOTAL_CALL_EXCL_IVR,
        COL_COST,
        COL_SLA_BREACH,
        COL_ABANDON,
        COL_ABANDON_10S,
        COL_RING_TIME,
    ]:
        if c in df.columns:
            df[c] = to_num(df[c])

    # Sort within groups by time
    df = df.sort_values([COL_CALL_ID, "__call_time_dt", COL_CALL_TIME])

    out_rows = []
    for call_id, g in df.groupby(COL_CALL_ID, sort=False):
        g = g.copy()
        # Compute base times
        call_start_time = g["__call_time_dt"].min()
        first_human_answer_time = find_first_human_answer_time(g, time_col="__call_time_dt")

        # Aggregate call direction: Inbound if any leg is Inbound/Inbound Queue/Internal, else Outbound
        if COL_DIRECTION in g:
            dir_norm_all = (
                g[COL_DIRECTION]
                .astype(str)
                .str.replace(r"\s+", " ", regex=True)
                .str.strip()
                .str.lower()
            )
            inbound_like = dir_norm_all.isin({"inbound", "inbound queue", "internal"}).any()
            agg_direction = "Inbound" if inbound_like else "Outbound"
        else:
            agg_direction = "Inbound"

        # Outbound answered flag (1 if any status Answered for outbound calls)
        if COL_STATUS in g:
            status_norm_all = (
                g[COL_STATUS]
                .astype(str)
                .str.replace(r"\s+", " ", regex=True)
                .str.strip()
                .str.lower()
            )
        else:
            status_norm_all = pd.Series(["" for _ in range(len(g))], index=g.index)
        outbound_call_answered = 1 if (agg_direction == "Outbound" and (status_norm_all == "answered").any()) else 0

        # Agent answered after queue
        agent_answered = 1 if pd.notna(first_human_answer_time) else 0

        # Outside working hours
        outside = 0
        if pd.notna(call_start_time):
            hr = int(call_start_time.hour)
            outside = 1 if (hr < 8 or hr >= 20) else 0

        # Aggregations (sums)
        # total_queue_wait will be computed after identifying 'Inbound Queue'+'Unanswered' rows to avoid duplication
        total_ring = float(g[COL_RING_TIME].sum(skipna=True)) if COL_RING_TIME in g else 0.0
        total_talk = float(g[COL_TALK_TIME].sum(skipna=True)) if COL_TALK_TIME in g else 0.0
        # For outbound calls, also include 'Talking' (text) duration summed to seconds
        if agg_direction == "Outbound" and COL_TALKING_TEXT in g:
            talk_text = g[COL_TALKING_TEXT]
            if not talk_text.empty:
                add_secs = 0.0
                for v in talk_text:
                    secs = _parse_hms_to_seconds(v)
                    if secs is not None:
                        add_secs += float(secs)
                total_talk += add_secs
        total_call_duration_excl = float(g[COL_TOTAL_CALL_EXCL_IVR].sum(skipna=True)) if COL_TOTAL_CALL_EXCL_IVR in g else 0.0
        cost_sum = float(g[COL_COST].sum(skipna=True)) if COL_COST in g else 0.0

        # Total queue unanswered: sum Talking seconds for Inbound Queue + Unanswered
        total_queue_unanswered = 0.0
        dir_norm_u = g[COL_DIRECTION].astype(str).str.replace(r"\s+", " ", regex=True).str.strip().str.lower()
        status_norm_u = g[COL_STATUS].astype(str).str.replace(r"\s+", " ", regex=True).str.strip().str.lower()
        mask_unanswered = (dir_norm_u == "inbound queue") & (status_norm_u == "unanswered")
        if COL_TALKING_TEXT in g:
            talk_unanswered = g.loc[mask_unanswered, COL_TALKING_TEXT]
            if not talk_unanswered.empty:
                for v in talk_unanswered:
                    secs = _parse_hms_to_seconds(v)
                    if secs is not None:
                        total_queue_unanswered += float(secs)

        # Compute total_queue_wait excluding rows accounted in total_queue_unanswered to avoid duplication
        if COL_WAIT_QUEUE in g:
            wait_series = g.loc[~mask_unanswered, COL_WAIT_QUEUE]
            total_queue_wait = float(wait_series.sum(skipna=True))
        else:
            total_queue_wait = 0.0

        # IVR time calculation
        mask_queue_wait = (g[COL_DIRECTION] == "Inbound Queue") & (g[COL_STATUS] == "Waiting")
        queue_positions = np.where(mask_queue_wait.values)[0]
        first_queue_idx = int(queue_positions[0]) if queue_positions.size > 0 else None

        ivr_indices = []
        if first_queue_idx is not None:
            subset = g.iloc[: first_queue_idx]
            for i, row in subset.iterrows():
                if (
                    row.get(COL_DIRECTION) == "Inbound"
                    and row.get(COL_STATUS) == "Answered"
                    and _ringing_is_zero(row.get(COL_RINGING_TEXT))
                ):
                    ivr_indices.append(i)
        else:
            for i, row in g.iterrows():
                cond = (
                    row.get(COL_DIRECTION) == "Inbound"
                    and row.get(COL_STATUS) == "Answered"
                    and _ringing_is_zero(row.get(COL_RINGING_TEXT))
                )
                if cond:
                    ivr_indices.append(i)
                else:
                    break

        ivr_secs_total = 0
        if ivr_indices:
            talk_series = g.loc[ivr_indices, COL_TALKING_TEXT] if COL_TALKING_TEXT in g else pd.Series([], dtype=object)
            if not talk_series.empty:
                for v in talk_series:
                    secs = _parse_hms_to_seconds(v)
                    if secs is not None:
                        ivr_secs_total += secs

        # Include total_queue_unanswered in both duration totals
        total_call_duration_excl_plus = total_call_duration_excl + float(total_queue_unanswered)
        total_call_duration_incl = total_call_duration_excl_plus + float(ivr_secs_total)
        # For outbound, also add ring time and total_talk (from numeric + text) to both durations
        if agg_direction == "Outbound":
            total_call_duration_excl_plus += float(total_talk) + float(total_ring)
            total_call_duration_incl += float(total_talk) + float(total_ring)

        # Flags (max)
        sla_breach = int(g[COL_SLA_BREACH].max(skipna=True)) if COL_SLA_BREACH in g else 0
        abandon = int(g[COL_ABANDON].max(skipna=True)) if COL_ABANDON in g else 0
        abandon_10s = int(g[COL_ABANDON_10S].max(skipna=True)) if COL_ABANDON_10S in g else 0

        # Environment: last non-empty
        env_value = last_non_empty(g[COL_ENV]) if COL_ENV in g else None

        # week: first non-null in time order
        wk_val = None
        if COL_WEEK in g:
            wk_val = first_non_null(g[COL_WEEK])

        # Derived date parts
        if pd.notna(call_start_time):
            start_day = call_start_time.date().isoformat()
            start_hour = int(call_start_time.hour)
            month = int(call_start_time.month)
            year = int(call_start_time.year)
        else:
            start_day = None
            start_hour = None
            month = None
            year = None

        out_rows.append(
            {
                "call_id": call_id,
                "call_start_time": None if pd.isna(call_start_time) else call_start_time.isoformat(sep=" ", timespec="seconds"),
                "outside_working_hours": outside,
                "Direction": agg_direction,
                "Outbound_call_answered": outbound_call_answered,
                "Inbound_call_answered": agent_answered,
                "first_agent_answer_time": None if (first_human_answer_time is None or pd.isna(first_human_answer_time)) else first_human_answer_time.isoformat(sep=" ", timespec="seconds"),
                "total_IVR": int(ivr_secs_total),
                "total_queue_unanswered": total_queue_unanswered,
                "total_queue_wait": total_queue_wait,
                "total_ring": total_ring,
                "total_talk": total_talk,
                "total_call_duration (excl. IVR)": total_call_duration_excl_plus,
                "total_call_duration (incl. IVR)": total_call_duration_incl,
                "cost_sum": cost_sum,
                "sla_breach": sla_breach,
                "abandon": abandon,
                "abandon_within_10s": abandon_10s,
                "environment": env_value,
                "start_day": start_day,
                "week": wk_val,
                "start_hour": start_hour,
                "month": month,
                "year": year,
            }
        )

    out_df = pd.DataFrame(out_rows)
    # Stable order
    out_df = out_df.sort_values(["call_start_time", "call_id"], na_position="last").reset_index(drop=True)
    return out_df


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalize calls.csv to one row per Call ID")
    default_in = Path(__file__).resolve().parent / "original_data" / "calls.csv"
    default_out = Path(__file__).resolve().parent / "calls_normalized.csv"
    parser.add_argument("--input", type=Path, default=default_in, help="Input calls.csv path")
    parser.add_argument("--output", type=Path, default=default_out, help="Output normalized CSV path")
    parser.add_argument("--sep", type=str, default=",", help="CSV delimiter (default ',')")
    parser.add_argument("--encoding", type=str, default="utf-8", help="CSV encoding")
    args = parser.parse_args()

    if not args.input.exists():
        raise SystemExit(f"Input CSV not found: {args.input}")

    print(f"[info] Reading: {args.input}")
    df = pd.read_csv(args.input, sep=args.sep, encoding=args.encoding, low_memory=False)
    # Normalize column names to avoid surprises (BOM/backticks/quotes/whitespace)
    def _clean_col(name: object) -> str:
        s = str(name)
        # remove BOM
        if s.startswith("\ufeff"):
            s = s.replace("\ufeff", "", 1)
        # strip whitespace and any stray quotes/backticks from both ends
        s = s.strip(" \t\r\n`'\"")
        return s
    rename_map = {c: _clean_col(c) for c in df.columns}
    if any(k != v for k, v in rename_map.items()):
        df = df.rename(columns=rename_map)
        print("[info] Normalized column names.")
    print(f"[ok] Loaded shape: {df.shape}")

    required_cols = [
        COL_CALL_ID,
        COL_CALL_TIME,
        COL_DIRECTION,
        COL_STATUS,
        COL_WAIT_QUEUE,
        COL_TOTAL_WAIT_Q_RING,
        COL_TALK_TIME,
        COL_TOTAL_CALL_EXCL_IVR,
        COL_COST,
        COL_SLA_BREACH,
        COL_ABANDON,
        COL_ABANDON_10S,
        COL_ENV,
        COL_WEEK,
        COL_RING_TIME,
        COL_RINGING_TEXT,
        COL_TALKING_TEXT,
    ]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        print(f"[warn] Missing expected columns: {missing}. Proceeding where possible.")

    normalized = normalize_calls(df)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    normalized.to_csv(args.output, index=False)
    print(f"[ok] Wrote: {args.output} (rows={len(normalized)})")


if __name__ == "__main__":
    main()


