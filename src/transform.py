import pandas as pd

# Charger les données
df = pd.read_csv("data/raw/weather_data.csv")

# Nettoyage des noms de colonnes
df.columns = [col.lower() for col in df.columns]

# Ajouter une date d'extraction
df["datetime"] = pd.Timestamp.now()

# Colonnes temporelles
df["year"] = df["datetime"].dt.year
df["month"] = df["datetime"].dt.month
df["day"] = df["datetime"].dt.day
df["weekday"] = df["datetime"].dt.day_name()

# Sauvegarde
df.to_csv("data/processed/weather_clean.csv", index=False)

print("✅ Données transformées")
print(df.head())