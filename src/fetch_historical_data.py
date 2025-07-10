# src/fetch_historical_data.py

import requests
import pandas as pd
import os

def fetch_historical_weather_data(latitude=53.08, longitude=8.80, start_date="2025-06-01", end_date="2025-06-30"):
    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": "temperature_2m,wind_speed_10m,shortwave_radiation",
        "timezone": "auto"
    }

    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame({
        "time": data["hourly"]["time"],
        "temperature_2m": data["hourly"]["temperature_2m"],
        "wind_speed_10m": data["hourly"]["wind_speed_10m"],
        "shortwave_radiation": data["hourly"]["shortwave_radiation"]
    })

    df["time"] = pd.to_datetime(df["time"])
    df.set_index("time", inplace=True)

    # Save to data/ folder
    output_dir = os.path.join(os.path.dirname(__file__), "../data")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "bremen_june_2025.csv")
    df.to_csv(output_path)

    print(f"[✓] Saved June 2025 historical data to: {output_path}")

    return df

if __name__ == "__main__":
    fetch_historical_weather_data()