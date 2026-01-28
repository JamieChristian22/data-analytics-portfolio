CREATE TABLE IF NOT EXISTS netflix_titles (
  show_id        TEXT PRIMARY KEY,
  type           TEXT,
  title          TEXT,
  director       TEXT,
  cast           TEXT,
  country        TEXT,
  date_added     DATE,
  release_year   INTEGER,
  rating         TEXT,
  duration       TEXT,
  listed_in      TEXT,
  description    TEXT,
  year_added     INTEGER,
  month_added    INTEGER,
  duration_min   INTEGER,
  seasons        INTEGER,
  primary_genre  TEXT
);
