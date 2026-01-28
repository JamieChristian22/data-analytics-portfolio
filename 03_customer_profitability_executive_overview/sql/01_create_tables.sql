CREATE TABLE IF NOT EXISTS orders (
  order_id          TEXT PRIMARY KEY,
  order_date        DATE,
  region            TEXT,
  state             TEXT,
  segment           TEXT,
  category          TEXT,
  quantity          INTEGER,
  discount          REAL,
  sales             REAL,
  profit            REAL,
  customer_id       TEXT,
  profit_ratio      REAL,
  profit_per_order  REAL,
  sales_per_customer REAL,
  year              INTEGER,
  month             TEXT
);
