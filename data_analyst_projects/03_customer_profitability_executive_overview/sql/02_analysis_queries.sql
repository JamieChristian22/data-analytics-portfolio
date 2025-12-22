-- Executive KPI rollup
SELECT
  SUM(sales) AS sales,
  SUM(profit) AS profit,
  ROUND(SUM(profit) / NULLIF(SUM(sales),0), 4) AS profit_ratio,
  ROUND(AVG(profit), 2) AS profit_per_order,
  ROUND(AVG(discount), 4) AS avg_discount,
  SUM(quantity) AS quantity
FROM orders;

-- Profit ratio by state (map inputs)
SELECT state,
       ROUND(SUM(profit) / NULLIF(SUM(sales),0), 4) AS profit_ratio,
       SUM(sales) AS sales,
       SUM(profit) AS profit
FROM orders
GROUP BY state
ORDER BY profit_ratio DESC;

-- Monthly Sales by Segment (small multiples)
SELECT DATE_TRUNC('month', order_date) AS month,
       segment,
       SUM(sales) AS sales
FROM orders
GROUP BY month, segment
ORDER BY month, segment;

-- Monthly Sales by Category (small multiples)
SELECT DATE_TRUNC('month', order_date) AS month,
       category,
       SUM(sales) AS sales
FROM orders
GROUP BY month, category
ORDER BY month, category;
