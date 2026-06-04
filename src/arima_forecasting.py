import pandas as pd
import matplotlib.pyplot as plt

from pmdarima import auto_arima

from sklearn.metrics import (
    mean_absolute_percentage_error,
    root_mean_squared_error
)

# Load data
df = pd.read_csv("data/TCS.NS.csv")

df["Date"] = pd.to_datetime(df["Date"])

# Split
train = df[df["Date"] < "2025-07-01"]
test = df[df["Date"] >= "2025-07-01"]

# Auto ARIMA
model = auto_arima(
    train["Close"],
    seasonal=False,
    trace=True,
    suppress_warnings=True
)

print(model.summary())

# Forecast
forecast = model.predict(n_periods=len(test))

# Metrics
rmse = root_mean_squared_error(
    test["Close"],
    forecast
)

mape = mean_absolute_percentage_error(
    test["Close"],
    forecast
)

print(f"\nRMSE : {rmse:.2f}")
print(f"MAPE : {mape*100:.2f}%")

# Plot
plt.figure(figsize=(12, 6))

plt.plot(
    train["Date"],
    train["Close"],
    label="Train"
)

plt.plot(
    test["Date"],
    test["Close"],
    label="Actual"
)

plt.plot(
    test["Date"],
    forecast,
    label="Forecast"
)

plt.legend()

plt.title("TCS ARIMA Forecast")

plt.tight_layout()

plt.savefig(
    "outputs/plots/TCS_ARIMA_forecast.png"
)

plt.show()
