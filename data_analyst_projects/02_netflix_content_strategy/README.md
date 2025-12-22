# Netflix Content Strategy (Catalog Analytics)

## Business Problem
Analyze a Netflix-style catalog to support content acquisition and regional growth. Identify content mix, ratings distribution, top genres, and top producing countries.

## Dataset
- **Raw**: Netflix-like titles with messy country casing, missing durations/dates, and duplicates.
- **Clean**: standardized country, parsed durations, year/month added, and primary genre extraction.

## Workflow
1. Clean and standardize catalog data
2. Derive duration metrics (minutes or seasons)
3. Compute distributions (type, rating, genre)
4. Trend titles added over time for growth insights

## Deliverables
- Raw + cleaned CSVs
- Python cleaning + analysis scripts
- SQL schema + dashboard queries
- Excel dashboard workbook
- Screenshot reference

## Key Insights (example outputs)
- Movies dominate the catalog mix (~2/3).
- TV-MA and TV-14 are most common.
- International Movies + Dramas lead genres.
- Additions accelerate after mid-2010s.

## Tech Stack
Python, SQL, Excel, Power BI-ready CSV
