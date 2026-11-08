-- Dimension Ville

CREATE TABLE IF NOT EXISTS dim_city (
    city_id SERIAL PRIMARY KEY,
    city_name VARCHAR(100) UNIQUE NOT NULL,
    country VARCHAR(100),
    latitude DECIMAL(10,6),
    longitude DECIMAL(10,6)
);

-- Dimension Date

CREATE TABLE IF NOT EXISTS dim_date (
    date_id SERIAL PRIMARY KEY,
    full_date DATE UNIQUE NOT NULL,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    day_of_week VARCHAR(20)
);

-- Table de Faits

CREATE TABLE IF NOT EXISTS fact_weather_air_quality (
    fact_id SERIAL PRIMARY KEY,

    city_id INTEGER REFERENCES dim_city(city_id),
    date_id INTEGER REFERENCES dim_date(date_id),

    temperature DECIMAL(5,2),
    feels_like DECIMAL(5,2),
    humidity INTEGER,
    pressure INTEGER,
    wind_speed DECIMAL(5,2),

    aqi INTEGER,
    pm2_5 DECIMAL(10,2),
    pm10 DECIMAL(10,2),
    co DECIMAL(10,2),
    no2 DECIMAL(10,2),
    o3 DECIMAL(10,2),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);