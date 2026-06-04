import pandas as pd
import matplotlib.pyplot as plt
import os

stocks = [
    "HDFCBANK.NS",
    "TCS.NS",
    "SUNPHARMA.NS",
    "MARUTI.NS",
    "HINDUNILVR.NS"
]

os.makedirs("outputs/plots", exist_ok=True)

for stock in stocks:

    df = pd.read_csv(f"data/{stock}.csv")

    df["Date"] = pd.to_datetime(df["Date"])

    # 30-day rolling volatility
    df["Rolling_STD"] = df["Close"].rolling(30).std()

    plt.figure(figsize=(12, 5))

    plt.plot(df["Date"], df["Rolling_STD"])

    plt.title(f"{stock} - 30 Day Rolling Volatility")
    plt.xlabel("Date")
    plt.ylabel("Rolling Std")

    plt.tight_layout()

    plt.savefig(
        f"outputs/plots/{stock}_rolling_std.png"
    )

    plt.close()

    print(f"Saved plot for {stock}")
