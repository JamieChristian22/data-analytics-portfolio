CREATE TABLE IF NOT EXISTS athens_listings (
  listing_id        TEXT PRIMARY KEY,
  neighborhood      TEXT,
  room_type         TEXT,
  price_eur         REAL,
  minimum_nights    INTEGER,
  number_of_reviews INTEGER,
  latitude          REAL,
  longitude         REAL,
  last_scraped      DATE
);
