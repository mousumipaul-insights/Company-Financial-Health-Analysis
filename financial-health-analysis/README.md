# 📊 Company Financial Health Analysis – DCF & Ratio Analysis

**Author:** Mousumi Paul  
**Project Type:** Personal Finance Project  
**Date:** December 2024

---

## 🔍 Project Overview

This project performs a comprehensive financial health analysis of a publicly listed FMCG company using **5 years of historical financial data** (FY2019–FY2023). It includes:

- Full Financial Statement Analysis (Income Statement, Balance Sheet, Cash Flow)
- Discounted Cash Flow (DCF) Model to estimate intrinsic value
- 15+ Financial Ratios across liquidity, profitability, leverage, and efficiency
- A structured management-style report with findings and recommendations

---

## 📁 Project Structure

```
financial-health-analysis/
│
├── data/
│   ├── raw/                        # Original financial data (Excel/CSV)
│   │   └── financial_statements.xlsx
│   └── processed/                  # Cleaned data ready for analysis
│       └── cleaned_financials.csv
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb      # Data loading & preprocessing
│   ├── 02_ratio_analysis.ipynb     # 15+ financial ratio calculations
│   ├── 03_dcf_model.ipynb          # DCF valuation model
│   └── 04_visualization.ipynb      # Charts & dashboards
│
├── src/
│   ├── ratio_calculator.py         # Functions for all financial ratios
│   ├── dcf_model.py                # DCF & WACC computation logic
│   └── utils.py                    # Helper functions
│
├── reports/
│   └── Financial_Health_Report.pdf # Final management-style report
│
├── outputs/
│   ├── charts/                     # Saved visualizations
│   └── tables/                     # Ratio summary tables (CSV/Excel)
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧮 Key Components

### 1. Financial Statement Analysis
- Income Statement: Revenue trends, EBITDA margin, net profit analysis
- Balance Sheet: Asset composition, working capital, equity structure
- Cash Flow Statement: Operating/investing/financing cash flows

### 2. DCF Valuation Model
| Parameter | Assumption |
|-----------|------------|
| Forecast Period | 5 Years |
| WACC | Computed from Cost of Equity (CAPM) + Cost of Debt |
| Terminal Growth Rate | 3–4% (sensitivity tested) |
| Sensitivity Analysis | WACC × Terminal Growth Rate grid |

### 3. Financial Ratios (15+)

| Category | Ratios |
|----------|--------|
| **Liquidity** | Current Ratio, Quick Ratio, Cash Ratio |
| **Profitability** | Gross Margin, EBITDA Margin, Net Margin, ROE, ROA, ROCE |
| **Leverage** | Debt-to-Equity, Interest Coverage, Debt-to-Assets |
| **Efficiency** | Asset Turnover, Inventory Turnover, Receivables Turnover, Days Sales Outstanding |

---

## ⚙️ Setup & Usage

### Prerequisites
```bash
pip install -r requirements.txt
```

### Run Analysis
```bash
# Step 1: Clean data
jupyter notebook notebooks/01_data_cleaning.ipynb

# Step 2: Ratio Analysis
jupyter notebook notebooks/02_ratio_analysis.ipynb

# Step 3: DCF Model
jupyter notebook notebooks/03_dcf_model.ipynb

# Step 4: Visualizations
jupyter notebook notebooks/04_visualization.ipynb
```

---

## 📦 Dependencies

See `requirements.txt` for full list. Core libraries:
- `pandas`, `numpy` – Data manipulation
- `matplotlib`, `seaborn` – Visualization
- `openpyxl` – Excel file handling
- `jupyter` – Notebook environment

---

## 📌 Key Findings (Summary)

> *(Update this section with your actual company findings)*

- The company demonstrated consistent **revenue growth of ~X% CAGR** over 5 years.
- **DCF intrinsic value** estimated at ₹XXX/share vs. market price of ₹XXX — suggesting X% upside/downside.
- **Liquidity position** remained healthy with current ratio above 1.5x throughout.
- **Leverage** was moderate with D/E ratio declining from X to Y, indicating improving financial stability.

---

## 📄 Report

The full management-style report is available in [`reports/Financial_Health_Report.pdf`](reports/Financial_Health_Report.pdf).

---

## 📬 Contact

**Mousumi Paul**  
[LinkedIn](https://linkedin.com/in/mousumi-paul) | [GitHub](https://github.com/mousumi-paul)
