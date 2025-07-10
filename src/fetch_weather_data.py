import requests
import pandas as pd

# Bremen coordinates
latitude = 53.08
longitude = 8.80

# API endpoint
url = "https://api.open-meteo.com/v1/forecast"
parameters = {
    "latitude": latitude,
    "longitude": longitude,
    "hourly": "temperature_2m,wind_speed_10m,shortwave_radiation",
    "timezone": "auto"
}

# Fetch data
response = requests.get(url, params=parameters)
data = response.json()

# Converting to DataFrame
df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature_2m": data["hourly"]["temperature_2m"],
    "wind_speed_10m": data["hourly"]["wind_speed_10m"],
    "shortwave_radiation": data["hourly"]["shortwave_radiation"]
})

# Format and save
df["time"] = pd.to_datetime(df["time"])
df.set_index("time", inplace=True)
df.to_csv("bremen_forecast.csv")

print("Saved forecast data to bremen_forecast.csv")