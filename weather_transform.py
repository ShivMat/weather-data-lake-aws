import json
import pandas as pd
import glob

raw_files = sorted(glob.glob("weather_raw_*.json"))
if not raw_files:
    raise FileNotFoundError("Run weather_ingestion.py first.")

latest_raw = raw_files[-1]
print("📌 Using raw file:", latest_raw)

with open(latest_raw, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame({
    "time": pd.to_datetime(data["hourly"]["time"]),
    "temperature_c": data["hourly"]["temperature_2m"],
    "humidity_pct": data["hourly"]["relative_humidity_2m"]
})

df = df.dropna()
df.to_csv("weather_cleaned.csv", index=False)

print("✅ Created weather_cleaned.csv")
print(df.head())
