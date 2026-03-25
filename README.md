# 📉 Tech Layoff Trend Analysis (2020–2025)

> **An end-to-end data analytics project** exploring five years of global tech industry layoffs — from the COVID-19 disruption through the post-AI-boom correction.

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://python.org)
[![SQLite](https://img.shields.io/badge/SQLite-3-blue?logo=sqlite)](https://sqlite.org)
[![Tableau](https://img.shields.io/badge/Tableau-Dashboard-orange?logo=tableau)](https://public.tableau.com)
[![License](https://img.shields.io/badge/Data-ODbL-green)](https://opendatacommons.org/licenses/odbl/)
[![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)]()

---

## 🧭 Project Overview

Tech layoffs between 2020 and 2025 tell a story that spans pandemic over-hiring, rising interest rates, AI-driven restructuring, and market corrections. This project analyzes **2,500+ layoff events across 55 countries and 28 industries** to uncover patterns that are actionable for job seekers, investors, and business analysts alike.

**Key questions this project answers:**
- Which industries and company stages were hit hardest — and when?
- How do layoff patterns differ between the COVID wave (2020) and the AI restructuring wave (2023–2024)?
- Are larger funding rounds correlated with bigger layoffs?
- Which geographies recovered fastest in headcount terms?

---

## 🗂️ Project Structure

```
tech-layoff-analysis/
│
├── data/
│   ├── raw/                    # Original CSV from Kaggle (gitignored)
│   └── processed/              # Cleaned output after ETL
│
├── notebooks/
│   ├── 01_eda_cleaning.ipynb   # Exploratory data analysis + data cleaning
│   └── 02_analysis.ipynb       # In-depth analysis + visualizations
│
├── sql/
│   ├── schema.sql              # SQLite table definitions
│   └── queries.sql             # Analysis queries (aggregations, window functions)
│
├── scripts/
│   ├── clean.py                # Standalone cleaning pipeline
│   └── load_to_sqlite.py       # Load cleaned CSV → SQLite DB
│
├── visuals/
│   └── screenshots/            # Tableau dashboard screenshots for README
│
├── docs/
│   └── project_plan.md         # Phased roadmap and task tracker
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Data Source | [Kaggle — swaptr/layoffs-2022](https://www.kaggle.com/datasets/swaptr/layoffs-2022) |
| Data Cleaning | Python (pandas, numpy) |
| Storage | SQLite |
| Analysis | Python (pandas), SQL |
| Visualization | Tableau Public + Matplotlib/Seaborn |
| Environment | Jupyter Notebook |
| Version Control | Git + GitHub |

---

## 📊 Dataset

**Source:** [layoffs.fyi](https://layoffs.fyi) via Kaggle (ODbL License)
**Rows:** ~2,500+ events | **Coverage:** 2020–2025 | **Countries:** 55 | **Industries:** 28

| Column | Description |
|---|---|
| `company` | Company name |
| `location` | City/region of HQ |
| `industry` | Sector (e.g., Consumer, Finance, Healthcare) |
| `total_laid_off` | Absolute headcount cut |
| `percentage_laid_off` | % of workforce affected |
| `date` | Date of layoff announcement |
| `stage` | Funding stage (Series A–J, IPO, Private Equity) |
| `country` | Country of HQ |
| `funds_raised` | Total funding raised (millions USD) |

**Known data quality issues (handled in cleaning):**
- Null values in `total_laid_off` and `percentage_laid_off` (~15% of rows)
- Inconsistent company name casing (e.g., `Salesforce` vs `salesforce`)
- Mixed date formats
- Duplicate entries from re-reported events

---

## 🔍 Analysis Highlights

### Phase 1: Data Cleaning
- Standardized company names and industry labels
- Handled nulls using stage-informed imputation strategies
- Parsed and normalized date fields
- Removed duplicates with deduplication logic

### Phase 2: SQL Analysis
Key queries run against SQLite:
- Rolling 90-day layoff totals by industry
- Top 10 companies by total headcount cut per year
- Companies that laid off 100% of workforce (effectively shut down)
- Correlation between funding stage and layoff percentage
- Country-level aggregations with YoY comparison

### Phase 3: Tableau Dashboard
*(Link to Tableau Public coming soon)*

Dashboard views:
1. **Timeline View** — Monthly layoff volume 2020–2025, annotated with macro events
2. **Industry Breakdown** — Treemap of total layoffs by sector
3. **Stage Analysis** — Which funding stages are most vulnerable?
4. **Geography Map** — Country-level heat map with layoff density
5. **Top Companies** — Bar chart race or ranked table by year

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Jupyter Notebook or JupyterLab
- Tableau Desktop or Tableau Public (free)

### Setup

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/tech-layoff-analysis.git
cd tech-layoff-analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add raw data
# Download layoffs_raw.csv from:
# https://www.kaggle.com/datasets/swaptr/layoffs-2022
# Save it to: data/raw/layoffs_raw.csv

# 4. Run the cleaning script
python scripts/clean.py

# 5. Load to SQLite
python scripts/load_to_sqlite.py

# 6. Open notebooks
jupyter notebook
```

---

## 📈 Key Findings

> *To be updated as analysis progresses.*

- **2022 saw the largest single-year layoff volume** in the dataset, driven by post-pandemic corrections at consumer tech giants
- **Series C–E companies** showed the highest average `percentage_laid_off`, suggesting mid-stage growth-phase companies were disproportionately exposed
- **The United States accounted for ~60% of all layoff events**, though India saw the highest proportional growth in events YoY
- **Consumer, Retail, and Transportation sectors** led in absolute headcount cuts; **Crypto and EdTech** led in company shutdowns (100% layoffs)

---

## 🧑‍💻 About This Project

This project was built as a portfolio piece to demonstrate end-to-end data analytics skills:
- **Data quality thinking** — real-world null handling, deduplication, and normalization
- **SQL fluency** — window functions, aggregations, CTEs
- **Python/pandas** — ETL pipeline, EDA, statistical summaries
- **Data storytelling** — Tableau dashboard designed for a business audience

**Author:** Talib Hussain
**LinkedIn:** [linkedin.com/in/talhussain](https://linkedin.com/in/talhussain)
**Contact:** tbhatti211@gmail.com

---

## 📄 License

Data sourced from [layoffs.fyi](https://layoffs.fyi) and distributed under the [Open Data Commons Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/). Analysis code is MIT licensed.

---

*Last updated: March 2026*