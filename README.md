# 🌦️ Weather & Air Quality Data Warehouse

An end-to-end Data Engineering project that collects weather and air quality data from the OpenWeather API, transforms and stores the data in a SQLite Data Warehouse, and provides insights through an interactive Streamlit dashboard.

---

## 📌 Project Overview

This project demonstrates a complete Data Engineering workflow:

- Extract weather and air quality data from OpenWeather APIs
- Transform and clean raw data using Pandas
- Load processed data into a SQLite Data Warehouse
- Perform analytical queries using SQL
- Visualize insights through an interactive Streamlit dashboard

The project follows a modern ETL architecture and implements a Star Schema Data Warehouse model.

---

## 🏗️ Architecture

```text
OpenWeather API
        │
        ▼
   Extract Layer
        │
        ▼
 Transform Layer
        │
        ▼
    Load Layer
        │
        ▼
SQLite Data Warehouse
        │
        ▼
 SQL Analytics
        │
        ▼
Streamlit Dashboard
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- SQLite
- SQL
- OpenWeather API
- Streamlit
- Plotly
- Git
- GitHub

---

## 📂 Project Structure

```text
weather-air-quality-data-warehouse/
│
├── src/
│   ├── extract_weather.py
│   ├── transform.py
│   └── load.py
│
├── data/
│
├── sql/
│
├── visualizations/
│   ├── dashboard_overview.png
│   └── dashboard_charts.png
│
├── dashboard.py
├── weather_warehouse.db
├── requirements.txt
├── README.md
│
├── tests/
├── notebooks/
├── dags/
└── logs/
```

---

## 🔄 ETL Pipeline

### Extract

The extraction layer retrieves:

- Current weather data
- Air quality data

for the following cities:

- Paris 🇫🇷
- London 🇬🇧
- Berlin 🇩🇪
- Madrid 🇪🇸
- New York 🇺🇸

### Transform

The transformation layer:

- Cleans raw data
- Standardizes formats
- Generates date attributes
- Creates analytical columns:
  - year
  - month
  - day
  - weekday

### Load

The processed dataset is loaded into a SQLite Data Warehouse using a Star Schema model.

---

## 🗄️ Data Warehouse Schema

### Dimension Table: dim_city

Stores city information.

| Column |
|----------|
| city |
| country |
| latitude |
| longitude |
| city_id |

### Dimension Table: dim_date

Stores date information.

| Column |
|----------|
| datetime |
| year |
| month |
| day |
| weekday |
| date_id |

### Fact Table: fact_weather

Stores weather and air quality metrics.

| Column |
|----------|
| city_id |
| date_id |
| temperature |
| feels_like |
| humidity |
| pressure |
| wind_speed |
| aqi |
| pm2_5 |
| pm10 |
| co |
| no2 |
| o3 |

---

## 📊 Dashboard Features

✅ Weather monitoring by city

✅ Air quality monitoring

✅ Temperature analysis

✅ Humidity analysis

✅ KPI indicators

✅ Interactive visualizations

✅ City comparison analytics

---

## 📸 Dashboard Preview

### KPI Dashboard

visualizations/dashboard_overview.png

---

### Weather & Air Quality Analysis

visualizations/dashboard_charts.png

---

## 📈 Key Insights

The dashboard automatically identifies:

- 🌍 Number of monitored cities
- 🌡️ Average temperature
- 💨 Average Air Quality Index (AQI)
- 💧 Average humidity
- 🌬️ Average wind speed
- 🔥 Hottest city
- 🌫️ Most polluted city

---

## 🌐 Data Source

Data is collected from:

- OpenWeather Current Weather API
- OpenWeather Air Pollution API

Official Documentation:

https://openweathermap.org/api

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/Alpha38diallo/weather-air-quality-data-warehouse.git
cd weather-air-quality-data-warehouse
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

Mac / Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENWEATHER_API_KEY=your_api_key
```

---

## ▶️ Run ETL Pipeline

### Extract

```bash
python src/extract_weather.py
```

### Transform

```bash
python src/transform.py
```

### Load

```bash
python src/load.py
```

---

## 📊 Launch Dashboard

```bash
streamlit run dashboard.py
```

---

## 🎯 Skills Demonstrated

- REST API Integration
- Data Extraction
- Data Transformation
- Data Cleaning
- ETL Pipelines
- Data Warehousing
- Star Schema Modeling
- SQL Analytics
- Dashboard Development
- Data Visualization
- Version Control with Git
- GitHub Project Management

---

## 🔮 Future Improvements

- Incremental Data Loading
- Historical Weather Tracking
- Daily Automated ETL Jobs
- Apache Airflow Integration
- Docker Containerization
- Cloud Deployment (AWS / Azure)
- Real-Time Data Pipelines

---

## 👨‍💻 Author

**Alpha Diallo**

GitHub:

https://github.com/Alpha38diallo

---

⭐ If you find this project useful, feel free to give it a star.