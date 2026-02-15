import requests
import json
from datetime import datetime

# Delray Beach, Florida coordinates (you can change later)
LAT = 26.46
LON = -80.07

url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={LAT}&longitude={LON}"
    "&hourly=temperature_2m,relative_humidity_2m"
    "&timezone=America/New_York"
)

response = requests.get(url, timeout=30)
response.raise_for_status()
data = response.json()

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
raw_filename = f"weather_raw_{timestamp}.json"

with open(raw_filename, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("✅ Raw weather data saved:", raw_filename)
