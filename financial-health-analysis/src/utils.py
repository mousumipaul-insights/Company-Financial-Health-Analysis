"""
utils.py
--------
Helper utilities for data loading, formatting, and export.
Author: Mousumi Paul | Dec 2024
"""

import pandas as pd
import matplotlib.pyplot as plt
import os


def load_financials(filepath: str, sheet_name: str = "Sheet1") -> pd.DataFrame:
    """Load financial data from Excel or CSV."""
    if filepath.endswith(".xlsx"):
        return pd.read_excel(filepath, sheet_name=sheet_name, index_col=0)
    elif filepath.endswith(".csv"):
        return pd.read_csv(filepath, index_col=0)
    else:
        raise ValueError("Unsupported file format. Use .xlsx or .csv")


def format_inr(value: float, crore: bool = True) -> str:
    """Format a number as Indian currency string."""
    suffix = " Cr" if crore else ""
    return f"₹{value:,.2f}{suffix}"


def save_table(df: pd.DataFrame, filename: str, output_dir: str = "outputs/tables/"):
    """Save a DataFrame as CSV to the outputs/tables directory."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, filename)
    df.to_csv(path)
    print(f"✅ Table saved: {path}")


def save_chart(fig, filename: str, output_dir: str = "outputs/charts/"):
    """Save a matplotlib figure to the outputs/charts directory."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, filename)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"✅ Chart saved: {path}")
    plt.close(fig)


def highlight_ratio(value: float, low: float, high: float) -> str:
    """Return color label based on ratio threshold."""
    if value < low:
        return "🔴 Below Benchmark"
    elif value > high:
        return "🟢 Above Benchmark"
    else:
        return "🟡 Within Range"
