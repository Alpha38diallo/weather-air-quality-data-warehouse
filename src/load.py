import sqlite3
import pandas as pd

# Connexion SQLite
conn = sqlite3.connect("weather_warehouse.db")

# Chargement des données transformées
df = pd.read_csv("data/processed/weather_clean.csv")

# -------------------
# DIM_CITY
# -------------------
dim_city = df[
    ["city", "country", "latitude", "longitude"]
].drop_duplicates()

dim_city["city_id"] = range(1, len(dim_city) + 1)

# -------------------
# DIM_DATE
# -------------------
dim_date = df[
    ["datetime", "year", "month", "day", "weekday"]
].drop_duplicates()

dim_date["date_id"] = range(1, len(dim_date) + 1)

# -------------------
# FACT_WEATHER
# -------------------
fact_weather = df.merge(
    dim_city,
    on=["city", "country", "latitude", "longitude"]
)

fact_weather = fact_weather.merge(
    dim_date,
    on=["datetime", "year", "month", "day", "weekday"]
)

fact_weather = fact_weather[
    [
        "city_id",
        "date_id",
        "temperature",
        "feels_like",
        "humidity",
        "pressure",
        "wind_speed",
        "aqi",
        "pm2_5",
        "pm10",
        "co",
        "no2",
        "o3"
    ]
]

# Sauvegarde SQLite
dim_city.to_sql("dim_city", conn, if_exists="replace", index=False)
dim_date.to_sql("dim_date", conn, if_exists="replace", index=False)
fact_weather.to_sql("fact_weather", conn, if_exists="replace", index=False)

conn.close()

print("✅ Data Warehouse créé avec succès")
print("✅ Tables : dim_city, dim_date, fact_weather")