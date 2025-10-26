from __future__ import annotations

import argparse
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd


def infer_format(series: pd.Series) -> str:
    if pd.api.types.is_datetime64_any_dtype(series):
        return "datetime"
    if pd.api.types.is_bool_dtype(series):
        return "bool"
    if pd.api.types.is_integer_dtype(series):
        return "int"
    if pd.api.types.is_float_dtype(series):
        return "float"
    if pd.api.types.is_object_dtype(series):
        sample = series.dropna().astype(str)
        sample = sample.head(200)
        if not sample.empty:
            parsed = pd.to_datetime(sample, errors="coerce", infer_datetime_format=True)
            if parsed.notna().mean() >= 0.8:
                return "datetime-like string"
        return "string"
    return str(series.dtype)


def _format_value(value: object) -> str:
    if isinstance(value, (pd.Timestamp,)):
        return value.isoformat(sep=" ", timespec="seconds")
    if isinstance(value, (np.floating, float)):
        # Limit precision for readability
        return f"{float(value):.6g}"
    if isinstance(value, (np.integer, int)):
        return str(int(value))
    s = str(value)
    s = s.replace("\n", " ").replace("\r", " ")
    if len(s) > 60:
        s = s[:57] + "..."
    # Escape markdown pipe
    s = s.replace("|", "\\|")
    return s


def sample_unique_values(series: pd.Series, max_values: int = 10) -> List[str]:
    if series.empty:
        return []
    s = series.dropna()
    if s.empty:
        return []
    # For numeric types, sort numerically; otherwise sort by string
    values = s.unique()
    try:
        if pd.api.types.is_numeric_dtype(s):
            values = np.sort(values)
        else:
            values = sorted(values, key=lambda v: str(v))
    except Exception:
        values = values[:]
    values = list(values)[: max_values]
    return [_format_value(v) for v in values]


def build_markdown_summary(df: pd.DataFrame, source: Path, max_samples: int) -> str:
    lines: List[str] = []
    lines.append(f"## EDA Summary for `{source.name}`")
    lines.append("")
    lines.append(f"- **rows**: {len(df)}")
    lines.append(f"- **columns**: {df.shape[1]}")
    lines.append("")
    lines.append("| Column | Format | Unique | Sample unique values |")
    lines.append("| - | - | -: | - |")
    for column_name in df.columns:
        series = df[column_name]
        fmt = infer_format(series)
        unique_count = series.nunique(dropna=True)
        samples = sample_unique_values(series, max_values=max_samples)
        sample_str = ", ".join(samples)
        # Escape markdown pipes in column names
        safe_col = str(column_name).replace("|", "\\|")
        lines.append(f"| {safe_col} | {fmt} | {unique_count} | {sample_str} |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a short Markdown EDA summary for calls_normalized.csv")
    default_input = Path(__file__).resolve().parent / "calls_normalized.csv"
    default_output = Path(__file__).resolve().parent / "calls_normalized_eda.md"
    parser.add_argument("--input", type=Path, default=default_input, help="Input normalized CSV path")
    parser.add_argument("--output", type=Path, default=default_output, help="Output Markdown file path")
    parser.add_argument("--sep", type=str, default=",", help="CSV delimiter (default ',')")
    parser.add_argument("--encoding", type=str, default="utf-8", help="CSV encoding")
    parser.add_argument("--max-samples", type=int, default=10, help="Max sample unique values per column")
    args = parser.parse_args()

    if not args.input.exists():
        raise SystemExit(f"Input CSV not found: {args.input}")

    print(f"[info] Reading: {args.input}")
    df = pd.read_csv(args.input, sep=args.sep, encoding=args.encoding, low_memory=False)
    print(f"[ok] Loaded shape: {df.shape}")

    md = build_markdown_summary(df, source=args.input, max_samples=args.max_samples)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(md, encoding="utf-8")
    print(f"[ok] Wrote: {args.output}")


if __name__ == "__main__":
    main()


