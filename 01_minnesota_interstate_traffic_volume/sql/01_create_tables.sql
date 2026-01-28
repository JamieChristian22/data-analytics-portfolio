-- PostgreSQL / SQLite-friendly schema
CREATE TABLE IF NOT EXISTS traffic_volume (
  date_time        TIMESTAMP PRIMARY KEY,
  traffic_volume   INTEGER,
  temp_f           REAL,
  precip_mm        REAL,
  snow_mm          REAL,
  weather_main     TEXT,
  holiday          TEXT,
  year             INTEGER,
  month            INTEGER,
  day              INTEGER,
  hour             INTEGER,
  day_name         TEXT,
  is_weekend       INTEGER
);
