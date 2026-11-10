import sqlite3
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Weather & Air Quality Dashboard",
    layout="wide"
)

conn = sqlite3.connect("weather_warehouse.db")

query = """
SELECT
    dc.city,
    dc.country,
    fw.temperature,
    fw.humidity,
    fw.pressure,
    fw.wind_speed,
    fw.aqi,
    fw.pm2_5,
    fw.pm10
FROM fact_weather fw
JOIN dim_city dc
ON fw.city_id = dc.city_id
"""

df = pd.read_sql(query, conn)

st.title("🌍 Weather & Air Quality Dashboard")

# KPI

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "🌍 Villes suivies",
        df["city"].nunique()
    )

with col2:
    st.metric(
        "🌡️ Température moyenne",
        f"{df['temperature'].mean():.2f} °C"
    )

with col3:
    st.metric(
        "💨 AQI moyen",
        f"{df['aqi'].mean():.2f}"
    )

with col4:
    st.metric(
        "💧 Humidité moyenne",
        f"{df['humidity'].mean():.0f}%"
    )

with col5:
    st.metric(
        "🌬️ Vent moyen",
        f"{df['wind_speed'].mean():.2f} m/s"
    )

col5, col6 = st.columns(2)

with col5:
    hottest_city = df.loc[df["temperature"].idxmax(), "city"]

    st.success(
        f"🔥 Ville la plus chaude : {hottest_city}"
    )

with col6:
    polluted_city = df.loc[df["aqi"].idxmax(), "city"]

    st.warning(
        f"🌫️ Ville la plus polluée : {polluted_city}"
    )

st.dataframe(df)

st.subheader("🌡️ Temperature by City")

fig_temp = px.bar(
    df,
    x="city",
    y="temperature",
    color="temperature",
    text="temperature"
)

st.plotly_chart(fig_temp, use_container_width=True)

st.subheader("💨 Air Quality Index")

fig_aqi = px.bar(
    df,
    x="city",
    y="aqi",
    color="aqi"
)

st.plotly_chart(fig_aqi, use_container_width=True)

st.subheader("💧 Humidity")

fig_humidity = px.bar(
    df,
    x="city",
    y="humidity",
    color="humidity"
)

st.plotly_chart(fig_humidity, use_container_width=True)