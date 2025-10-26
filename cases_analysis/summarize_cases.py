from pathlib import Path
import warnings

import pandas as pd


def resolve_cases_csv_path() -> Path:
    """Return absolute path to original_data/cases.csv relative to this file."""
    return Path(__file__).resolve().parents[1] / "original_data" / "cases.csv"


def is_datetime_like(series: pd.Series) -> bool:
    """Heuristically determine if a series is datetime-like."""
    if pd.api.types.is_datetime64_any_dtype(series):
        return True
    if series.dtype == object:
        non_null = series.dropna()
        if non_null.empty:
            return False
        sample = non_null.sample(min(1000, len(non_null)), random_state=0)
        parsed = pd.to_datetime(sample, errors="coerce", infer_datetime_format=True, utc=False)
        success_ratio = parsed.notna().mean()
        return success_ratio >= 0.9
    return False


def summarize_dataframe_markdown(df: pd.DataFrame) -> str:
    lines = []
    lines.append("# Cases CSV Summary")
    lines.append("")
    lines.append(f"Dataset shape: {df.shape[0]:,} rows x {df.shape[1]:,} columns")
    lines.append("")
    lines.append("## Columns")
    lines.append("")

    for column_name in df.columns:
        column = df[column_name]
        non_null_count = int(column.notna().sum())
        missing_count = int(column.isna().sum())
        missing_pct = (missing_count / len(df)) * 100 if len(df) else 0.0

        lines.append(f"### {column_name}")
        lines.append("")
        lines.append(f"- dtype: `{column.dtype}`")
        lines.append(f"- non-null: {non_null_count:,}")
        lines.append(f"- missing: {missing_count:,} ({missing_pct:.2f}%)")

        if pd.api.types.is_numeric_dtype(column):
            mean_value = column.mean()
            median_value = column.median()
            std_value = column.std()
            min_value = column.min()
            max_value = column.max()
            lines.append("- numeric stats:")
            lines.append(f"  - mean: {mean_value:.6g}")
            lines.append(f"  - median: {median_value:.6g}")
            lines.append(f"  - std: {std_value:.6g}")
            lines.append(f"  - min: {min_value}")
            lines.append(f"  - max: {max_value}")
        elif is_datetime_like(column):
            parsed = pd.to_datetime(column, errors="coerce", infer_datetime_format=True, utc=False)
            min_dt = parsed.min()
            max_dt = parsed.max()
            lines.append("- datetime range:")
            lines.append(f"  - min: {min_dt}")
            lines.append(f"  - max: {max_dt}")
        else:
            non_null = column.dropna()
            unique_values = non_null.unique()
            unique_count = len(unique_values)
            lines.append(f"- unique values: {unique_count:,}")
            if unique_count <= 50:
                preview_values = ", ".join(sorted(map(lambda v: str(v), unique_values)))
                lines.append(f"- values: {preview_values}")
            else:
                top_counts = non_null.value_counts().head(20)
                lines.append("- top 20 values:")
                for idx, cnt in top_counts.items():
                    lines.append(f"  - {str(idx)}: {int(cnt)}")

        lines.append("")

    return "\n".join(lines)


def main() -> None:
    csv_path = resolve_cases_csv_path()
    if not csv_path.exists():
        raise FileNotFoundError(f"Could not find cases.csv at: {csv_path}")

    # Suppress pandas and parsing warnings to keep output clean
    warnings.filterwarnings("ignore")

    df = pd.read_csv(csv_path, low_memory=False)
    markdown = summarize_dataframe_markdown(df)

    out_path = Path(__file__).resolve().parent / "cases_summary.md"
    out_path.write_text(markdown, encoding="utf-8")


if __name__ == "__main__":
    main()


