import pandas as pd
from prophet import Prophet
from sklearn.metrics import (
    mean_absolute_percentage_error,
    root_mean_squared_error
)
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/TCS.NS.csv")

df["Date"] = pd.to_datetime(df["Date"])

# Prophet format
prophet_df = df[["Date", "Close"]].copy()
prophet_df.columns = ["ds", "y"]

# Split
train = prophet_df[prophet_df["ds"] < "2025-07-01"]
test = prophet_df[prophet_df["ds"] >= "2025-07-01"]

# Train model
model = Prophet()

model.fit(train)

# Forecast
future = model.make_future_dataframe(
    periods=len(test),
    freq="B"
)

forecast = model.predict(future)

predictions = forecast["yhat"].tail(len(test)).values

# Metrics
rmse = root_mean_squared_error(
    test["y"],
    predictions
)

mape = mean_absolute_percentage_error(
    test["y"],
    predictions
)

print(f"RMSE : {rmse:.2f}")
print(f"MAPE : {mape*100:.2f}%")

# Plot
plt.figure(figsize=(12, 6))

plt.plot(
    train["ds"],
    train["y"],
    label="Train"
)

plt.plot(
    test["ds"],
    test["y"],
    label="Actual"
)

plt.plot(
    test["ds"],
    predictions,
    label="Prophet Forecast"
)

plt.legend()

plt.title("TCS Prophet Forecast")

plt.tight_layout()

plt.savefig(
    "outputs/plots/TCS_Prophet_forecast.png"
)

plt.show()
