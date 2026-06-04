import pandas as pd
import warnings

from pmdarima import auto_arima
from prophet import Prophet

from sklearn.metrics import (
    mean_absolute_percentage_error,
    root_mean_squared_error
)

warnings.filterwarnings("ignore")

stocks = [
    "HDFCBANK.NS",
    "TCS.NS",
    "SUNPHARMA.NS",
    "MARUTI.NS",
    "HINDUNILVR.NS"
]

results = []

for stock in stocks:

    print(f"\nProcessing {stock}")

    df = pd.read_csv(f"data/{stock}.csv")

    df["Date"] = pd.to_datetime(df["Date"])

    train = df[df["Date"] < "2025-07-01"]
    test = df[df["Date"] >= "2025-07-01"]

    # ==================================================
    # ARIMA
    # ==================================================

    try:

        arima_model = auto_arima(
            train["Close"],
            seasonal=False,
            suppress_warnings=True,
            error_action="ignore",
            trace=False
        )

        arima_forecast = arima_model.predict(
            n_periods=len(test)
        )

        arima_rmse = root_mean_squared_error(
            test["Close"],
            arima_forecast
        )

        arima_mape = mean_absolute_percentage_error(
            test["Close"],
            arima_forecast
        )

        results.append([
            stock,
            "ARIMA",
            round(arima_rmse, 2),
            round(arima_mape * 100, 2)
        ])

        print(
            f"ARIMA Complete | "
            f"RMSE={arima_rmse:.2f} | "
            f"MAPE={arima_mape*100:.2f}%"
        )

    except Exception as e:

        print(f"ARIMA Failed: {e}")

    # ==================================================
    # PROPHET
    # ==================================================

    try:

        prophet_df = df[["Date", "Close"]].copy()

        prophet_df.columns = [
            "ds",
            "y"
        ]

        train_prophet = prophet_df[
            prophet_df["ds"] < "2025-07-01"
        ]

        test_prophet = prophet_df[
            prophet_df["ds"] >= "2025-07-01"
        ]

        prophet_model = Prophet()

        prophet_model.fit(train_prophet)

        future = prophet_model.make_future_dataframe(
            periods=len(test_prophet),
            freq="B"
        )

        forecast = prophet_model.predict(
            future
        )

        prophet_predictions = (
            forecast["yhat"]
            .tail(len(test_prophet))
            .values
        )

        prophet_rmse = root_mean_squared_error(
            test_prophet["y"],
            prophet_predictions
        )

        prophet_mape = mean_absolute_percentage_error(
            test_prophet["y"],
            prophet_predictions
        )

        results.append([
            stock,
            "Prophet",
            round(prophet_rmse, 2),
            round(prophet_mape * 100, 2)
        ])

        print(
            f"Prophet Complete | "
            f"RMSE={prophet_rmse:.2f} | "
            f"MAPE={prophet_mape*100:.2f}%"
        )

    except Exception as e:

        print(f"Prophet Failed: {e}")

# ==================================================
# SAVE RESULTS
# ==================================================

results_df = pd.DataFrame(
    results,
    columns=[
        "Stock",
        "Model",
        "RMSE",
        "MAPE"
    ]
)

results_df.to_csv(
    "outputs/reports/model_results.csv",
    index=False
)

print("\n")
print("=" * 50)
print("MODEL COMPARISON COMPLETE")
print("=" * 50)

print(results_df)
