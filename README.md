# 🌦 Weather Data Lake & Analytics Pipeline (AWS + Python)

## Project Overview
Built an end-to-end data engineering pipeline that ingests real-time weather data from a public API, stores raw and cleaned data in Amazon S3, and performs SQL analytics using AWS Athena.

---

## Architecture
Open-Meteo API  
⬇  
Python Ingestion  
⬇  
S3 Raw Layer  
⬇  
Python Transformation  
⬇  
S3 Cleaned Layer  
⬇  
Athena SQL Analytics  

---

## Technologies Used
- Python (requests, pandas)
- AWS S3
- AWS Athena
- SQL
- JSON & CSV

---

## Data Lake Structure

weather-data/
    raw/
    cleaned/
athena-results/

---

## Results
- Successfully processed 168 weather records
- Generated daily average temperature trends
- Validated data using row count and null checks

---

## Sample SQL Queries

SELECT COUNT(*) FROM weather_hourly;

SELECT date(time) AS day, AVG(temperature_c) AS avg_temp
FROM weather_hourly
GROUP BY date(time)
ORDER BY day;
