"""
load_to_sqlite.py — Load cleaned CSV into SQLite database
Author: Talib Hussain

Reads: data/processed/layoffs_clean.csv
Writes: data/layoffs.db
"""

import pandas as pd
import sqlite3
import os

CLEAN_PATH = "data/processed/layoffs_clean.csv"
DB_PATH = "data/layoffs.db"


def load_to_sqlite(csv_path: str, db_path: str):
    df = pd.read_csv(csv_path)
    print(f"[LOAD] {len(df)} rows from {csv_path}")

    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)

    # Write to SQLite — replace table if exists
    df.to_sql("layoffs", conn, if_exists="replace", index=False)

    # Create indexes for common query patterns
    conn.execute("CREATE INDEX IF NOT EXISTS idx_year     ON layoffs(year)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_industry ON layoffs(industry)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_country  ON layoffs(country)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_stage    ON layoffs(stage)")
    conn.commit()

    # Verify
    count = conn.execute("SELECT COUNT(*) FROM layoffs").fetchone()[0]
    print(f"[DB] Rows in SQLite 'layoffs' table: {count}")
    print(f"[DB] Database saved to {db_path}")

    conn.close()


if __name__ == "__main__":
    load_to_sqlite(CLEAN_PATH, DB_PATH)