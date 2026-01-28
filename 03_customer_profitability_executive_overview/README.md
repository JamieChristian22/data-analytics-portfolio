# Executive Overview - Customer Profitability

## Business Problem
Provide an executive dashboard for profitability performance across regions/states, segments, and categories. Identify where profit ratios are strongest/weakest and how discounting impacts margin.

## Dataset
- **Raw**: order-level dataset (2014–2017) with mixed types, missing values, upper-case states, and duplicates.
- **Clean**: typed fields, imputed profit where missing, derived profit_ratio and time fields.

## Workflow
1. Clean raw orders
2. Compute KPI layer and derived metrics
3. Build state-level profit ratio map inputs
4. Build monthly trends by segment and category

## Deliverables
- `data/raw/orders_raw.csv` + `data/clean/orders_clean.csv`
- `python/01_clean_data.py` + `python/02_analysis.py`
- SQL schema + dashboard queries
- Excel executive dashboard
- Power BI screenshot + PBIX (if available)

## Key Insights (example outputs)
- Technology tends to have higher average order values, but margin is sensitive to discount.
- Some states show negative profit ratios (returns/discount pressure).
- Segment mix shifts over time; Corporate often drives higher ticket sizes.

## Tech Stack
Python, SQL, Excel, Power BI
