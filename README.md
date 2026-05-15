# 📉 Tech Layoff Trend Analysis (2020–2025)

> **An end-to-end data analytics project** exploring five years of global tech industry layoffs — from the COVID-19 disruption through the post-AI-boom correction.

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://python.org)
[![SQLite](https://img.shields.io/badge/SQLite-3-blue?logo=sqlite)](https://sqlite.org)
[![Tableau](https://img.shields.io/badge/Tableau-Dashboard-orange?logo=tableau)](https://public.tableau.com)
[![License](https://img.shields.io/badge/Data-ODbL-green)](https://opendatacommons.org/licenses/odbl/)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen)]()

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
├── dashboard
│   └── Tech lay off analysis 2020-2026.twb # Tableau Dashboard file 
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
**Interactive dashboard complete** — visualize layoff trends across industries, funding stages, and geography.

---

## 📈 Key Findings

- **2022 saw the largest single-year layoff volume** in the dataset, driven by post-pandemic corrections at consumer tech giants
- **Series C–E companies** showed the highest average `percentage_laid_off`, suggesting mid-stage growth-phase companies were disproportionately exposed
- **The United States accounted for ~60% of all layoff events**, though India saw the highest proportional growth in events YoY
- **Consumer, Retail, and Transportation sectors** led in absolute headcount cuts; **Crypto and EdTech** led in company shutdowns (100% layoffs)

---

## 📊 Tableau Dashboard

**Interactive dashboard built in Tableau** — explore 2,500+ layoff events across industries, funding stages, and time periods.

### Dashboard Views
- **KPI Cards:** Total events (3,617), total headcount (843K+), unique companies (2,497), countries affected (61)
- **Layoffs Over Time:** Line chart by industry (2020–2026) with logarithmic scale and interactive year filter
- **Top Industries:** Ranked bar chart of industries by total layoffs
- **Funding Stage Analysis:** Breakdown of layoffs by company stage (Post-IPO, Acquired, Series rounds, etc.)

### Key Features
- **Global year filter** — adjust timeline, all charts update in real-time
- **Interactive tooltips** — hover to see detailed metrics (industry, total laid off, percentage)
- **Color-coded theme** — brown/orange/red palette reflects "alarm" narrative (layoffs = disruption, not growth)
- **2-column layout** — left side tells the trend story, right side shows dimensional breakdowns

### How to View
1. Download `Tech lay off analysis 2020-2026.twb` from `/dashboard/` folder
2. Open in **Tableau Desktop** (recommended) or **Tableau Public** (free)
3. Use filters to drill into specific years or time periods
4. Hover over charts for detailed metrics

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Jupyter Notebook or JupyterLab
- Tableau Desktop or Tableau Public (free)

### Setup

```bash
# 1. Clone the repo
git clone https://github.com/tbhatti211-wq/tech-layoff-analysis.git
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

*Last updated: May 2026*