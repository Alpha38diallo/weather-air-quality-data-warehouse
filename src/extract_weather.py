import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

CITIES = [
    "Paris",
    "London",
    "Berlin",
    "Madrid",
    "New York"
]

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

weather_data = []

for city in CITIES:
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]

        air_url = (
        f"https://api.openweathermap.org/data/2.5/air_pollution"
           f"?lat={lat}&lon={lon}&appid={API_KEY}"
)

        air_response = requests.get(air_url)
        air_data = air_response.json()

        aqi = air_data["list"][0]["main"]["aqi"]

        pm2_5 = air_data["list"][0]["components"]["pm2_5"]
        pm10 = air_data["list"][0]["components"]["pm10"]

        co = air_data["list"][0]["components"]["co"]
        no2 = air_data["list"][0]["components"]["no2"]
        o3 = air_data["list"][0]["components"]["o3"]

        weather_data.append({
            "city": city,
            "country": data["sys"]["country"],
            "latitude": data["coord"]["lat"],
            "longitude": data["coord"]["lon"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind_speed": data["wind"]["speed"],

            "aqi": aqi,
            "pm2_5": pm2_5,
            "pm10": pm10,
            "co": co,
            "no2": no2,
            "o3": o3
        })

        print(f"✅ {city} récupérée")

    else:
        print(f"❌ Erreur sur {city}")
        print(response.status_code)
        print(response.text)
df = pd.DataFrame(weather_data)

df.to_csv(
    "data/raw/weather_data.csv",
    index=False
)

print("\n✅ Données météo sauvegardées")
print(df.head())