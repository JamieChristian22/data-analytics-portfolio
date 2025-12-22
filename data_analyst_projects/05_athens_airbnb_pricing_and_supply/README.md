# Athens Airbnb — Pricing & Supply

## Business Problem
Analyze how pricing varies by neighborhood and where listing supply is concentrated. Provide actionable recommendations for hosts (pricing strategy) and for platform ops (supply expansion targets).

## Dataset
- **Raw**: Athens listings with messy euro-formatted prices, missing neighborhoods, duplicates, and extreme outliers.
- **Clean**: standardized neighborhood names, numeric prices, outlier handling (p99 cap), typed fields.

## Workflow
1. Clean listings + price field
2. Compute avg price per neighborhood + listing counts
3. Identify premium neighborhoods and supply hotspots
4. Package SQL queries + Excel dashboard

## Deliverables
- Raw + cleaned CSVs
- Python scripts
- SQL schema + analysis queries
- Excel dashboard workbook
- Screenshot reference

## Key Insights (example outputs)
- Premium neighborhoods (e.g., Plaka/Kolonaki/Syntagma) command higher nightly rates.
- Supply is concentrated near the city center.
- Outlier control improves interpretability for pricing decisions.

## Tech Stack
Python, SQL, Excel, Power BI-ready CSV
