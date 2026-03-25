"""
clean.py — Tech Layoff Analysis: Data Cleaning Pipeline
Author: Talib Hussain

Reads: data/raw/layoffs_raw.csv
Writes: data/processed/layoffs_clean.csv
"""

import pandas as pd
import numpy as np
import os

RAW_PATH = "data/raw/layoffs_raw.csv"
CLEAN_PATH = "data/processed/layoffs_clean.csv"


def load_raw(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"[LOAD] Shape: {df.shape}")
    print(f"[LOAD] Columns: {list(df.columns)}")
    return df


def clean(df: pd.DataFrame) -> pd.DataFrame:

    # 1. Strip whitespace — fix for pandas deprecation warning
    str_cols = df.select_dtypes(include="str").columns
    df[str_cols] = df[str_cols].apply(lambda col: col.str.strip())

    # 2. Standardize company names
    df["company"] = df["company"].str.title()

    # 3. Normalize industry labels
    industry_map = {
        "Crypto": "Crypto",
        "Cryptocurrency": "Crypto",
        "Fin-Tech": "FinTech",
        "Finance": "Finance",
    }
    df["industry"] = df["industry"].replace(industry_map)

    # 4. Parse dates
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month

    # 5. Coerce numerics
    df["total_laid_off"] = pd.to_numeric(df["total_laid_off"], errors="coerce")
    df["percentage_laid_off"] = pd.to_numeric(df["percentage_laid_off"], errors="coerce")
    df["funds_raised"] = pd.to_numeric(df["funds_raised"], errors="coerce")

    # 6. Drop exact duplicates
    before = len(df)
    df = df.drop_duplicates()
    print(f"[CLEAN] Dropped {before - len(df)} duplicate rows")

    # 7. Drop rows where BOTH layoff fields are null (no analytical value)
    before = len(df)
    df = df.dropna(subset=["total_laid_off", "percentage_laid_off"], how="all")
    print(f"[CLEAN] Dropped {before - len(df)} rows where both layoff fields are null")

    # 8. Flag rows where only one field is null (keep but note)
    df["partial_data"] = (
        df["total_laid_off"].isnull() | df["percentage_laid_off"].isnull()
    )
    print(f"[CLEAN] Rows with partial layoff data: {df['partial_data'].sum()}")

    # 9. Drop the redundant source column (URL noise, not needed for analysis)
    if "source" in df.columns:
        df = df.drop(columns=["source"])

    print(f"\n[CLEAN] Final shape: {df.shape}")
    return df


def summarize_nulls(df: pd.DataFrame):
    print("\n[NULL SUMMARY]")
    print(df.isnull().sum().to_string())


def save(df: pd.DataFrame, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"\n[SAVE] Cleaned data saved to {path} ({len(df)} rows)")


if __name__ == "__main__":
    df = load_raw(RAW_PATH)
    summarize_nulls(df)
    df_clean = clean(df)
    summarize_nulls(df_clean)
    save(df_clean, CLEAN_PATH)