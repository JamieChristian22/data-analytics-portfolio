CREATE TABLE IF NOT EXISTS baby_names (
  year        INTEGER,
  gender      TEXT,
  name        TEXT,
  occurrences INTEGER,
  PRIMARY KEY (year, gender, name)
);
