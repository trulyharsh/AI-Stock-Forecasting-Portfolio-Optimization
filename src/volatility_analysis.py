import pandas as pd
import numpy as np

stocks = [
    "HDFCBANK.NS",
    "TCS.NS",
    "SUNPHARMA.NS",
    "MARUTI.NS",
    "HINDUNILVR.NS"
]

results = []

for stock in stocks:

    df = pd.read_csv(f"data/{stock}.csv")

    # Log Returns
    df["Log_Return"] = np.log(
        df["Close"] /
        df["Close"].shift(1)
    )

    # 30-Day Rolling Volatility
    df["Volatility"] = (
        df["Log_Return"]
        .rolling(30)
        .std()
    )

    avg_vol = df["Volatility"].mean()

    results.append([
        stock,
        round(avg_vol, 6)
    ])

    print(
        f"{stock} | "
        f"Average Volatility = {avg_vol:.6f}"
    )

vol_df = pd.DataFrame(
    results,
    columns=[
        "Stock",
        "Average_Volatility"
    ]
)

vol_df = vol_df.sort_values(
    by="Average_Volatility"
)

vol_df.to_csv(
    "outputs/reports/volatility_results.csv",
    index=False
)

print("\n")
print(vol_df)
