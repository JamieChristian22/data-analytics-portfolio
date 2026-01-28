import pandas as pd

RAW_PATH = "../data/raw/baby_names_raw.csv"
OUT_PATH = "../data/clean/baby_names_clean.csv"

df = pd.read_csv(RAW_PATH).drop_duplicates(subset=["year","gender","name"])

df["gender"] = (df["gender"]
                .replace({"Male":"M","Female":"F"})
                .astype(str).str.upper().str[0])

df["name"] = df["name"].astype(str).str.title().str.strip()
df["year"] = pd.to_numeric(df["year"], errors="coerce").astype(int)
df["occurrences"] = pd.to_numeric(df["occurrences"], errors="coerce")

med = df.groupby(["gender","name"])["occurrences"].median()

missing = df["occurrences"].isna()
df.loc[missing, "occurrences"] = df.loc[missing].apply(
    lambda r: med.get((r["gender"], r["name"]), 200.0),
    axis=1
)

df["occurrences"] = df["occurrences"].round(0).astype(int)

df.to_csv(OUT_PATH, index=False)
print(f"Saved cleaned dataset to: {OUT_PATH}")
