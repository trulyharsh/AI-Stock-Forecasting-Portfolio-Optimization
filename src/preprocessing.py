import pandas as pd

stocks = [
    "HDFCBANK.NS",
    "TCS.NS",
    "SUNPHARMA.NS",
    "MARUTI.NS",
    "HINDUNILVR.NS"
]

for stock in stocks:

    df = pd.read_csv(f"data/{stock}.csv")

    # Date conversion
    df["Date"] = pd.to_datetime(df["Date"])

    # Missing values
    df = df.ffill().bfill()

    # Train-Test Split
    train = df[df["Date"] < "2025-07-01"]

    test = df[df["Date"] >= "2025-07-01"]

    print("\n")
    print(stock)
    print("Train:", train.shape)
    print("Test :", test.shape)
