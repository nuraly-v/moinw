# 🌦️ Weather Forecast Mini-Project — Bremen, June 2025

This project explores and models hourly weather data for Bremen, Germany, using real-world meteorological variables. It simulates part of the analysis and modeling workflow relevant to short-term forecasting in the energy trading sector — such as estimating temperature, solar potential, or wind variability based on atmospheric data.

---

## Project Goals

- Retrieve and process historical weather data (hourly resolution)
- Explore trends and relationships between temperature, wind, and solar radiation
- Train predictive models to forecast next-day weather conditions
- Gain insights into how weather can influence energy systems (e.g., renewables)

---

## Location

- **Bremen, Germany**
- Timezone: Auto-adjusted (CET/CEST)
- Coordinates: `latitude=53.08`, `longitude=8.80`

---

## Time Range

- **June 1 – June 30, 2025**
- Data granularity: **hourly**

---

## Dataset

Fetched via the [`Open-Meteo Archive API`](https://open-meteo.com/):

- `temperature_2m` (°C)
- `wind_speed_10m` (m/s)
- `shortwave_radiation` (W/m²)

Saved to: `data/bremen_june_2025.csv`

---

## Tools & Libraries

- **Python** 3.x
- `pandas`, `matplotlib`, `seaborn`
- `scikit-learn`

---

## Analysis Highlights

- Visualized hourly and daily trends for all variables
- Identified strong correlation between **solar radiation** and **temperature** (r = 0.84)
- Found moderate correlation between **wind** and other variables (r = 0.56)
- Detected consistent diurnal cycles in solar and temperature patterns

---

## Modeling Overview

### 1. **Linear Regression**

- Target: Predict **average temperature on June 30**
- Features: Previous day’s (`t-1`) temperature, wind, radiation
- Result: Baseline model with modest accuracy but high bias

### 2. **Random Forest Regressor**

- Improved performance by capturing **non-linear dependencies**
- Feature importance: Prior-day **temperature** and **radiation** were most predictive
- Reduced absolute prediction error for June 30 significantly

---

## Results

| Date       | Model Type    | Predicted Temp (°C) | Actual Temp (°C) | Error (°C) |
| ---------- | ------------- | ------------------- | ---------------- | ---------- |
| 2025-06-30 | Linear Model  | 19.27               | 18.22            | 1.06       |
| 2025-06-30 | Random Forest | 18.81               | 18.22            | 0.60 ✅    |

---

## Key Insights

- **Solar radiation** is a strong leading indicator for surface temperature
- **Lagged weather data** (t-1) is often sufficient for 1-day-ahead predictions
- Simple models like **Random Forests** can perform surprisingly well on small, structured datasets

---

## Project Structure

```

moinw/
│
├── data/
│   └── bremen_forecast.csv
│   └── bremen_june_2025.csv
├── notebooks/
│   └── weather_analysis.ipynb
│   └── weather_june_analysis_RF.ipynb
│   └── weather_june_analysis.ipynb
├── src/
│   └── fetch_weather_data.py
│   └── fetch_historical_data.py
├── visuals/
│   └── Daily_averages_June_2025.png
│   └── June_2025_predictions_LinearRegression.png
│   └── June_2025_predictions_RF.png
│   └── Plot_June_2025.png
├── README.md
└── requirements.txt

```

---

## How to Run

1. Clone the repo:

```bash
git clone https://github.com/nuraly-v/moinw.git
```

2. Create a virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

3. Fetch historical data:

```bash
python src/fetch_historical_data.py
```

4. Run the notebook:

```
notebooks/weather_june_analysis.ipynb
```

---

## License

MIT License — feel free to reuse, fork, or extend.
