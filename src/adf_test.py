import pandas as pd
from statsmodels.tsa.stattools import adfuller

stocks = [
    "HDFCBANK.NS",
    "TCS.NS",
    "SUNPHARMA.NS",
    "MARUTI.NS",
    "HINDUNILVR.NS"
]

for stock in stocks:

    df = pd.read_csv(f"data/{stock}.csv")

    df["Close_Diff"] = df["Close"].diff()

    diff_series = df["Close_Diff"].dropna()

    result = adfuller(diff_series)

    print("\n" + "="*50)
    print(stock)

    print(f"ADF Statistic : {result[0]:.4f}")
    print(f"P-value       : {result[1]:.6f}")

    if result[1] < 0.05:
        print("Stationary After Differencing ✅")
    else:
        print("Still Non-Stationary ❌")
