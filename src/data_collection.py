import yfinance as yf
import os

stocks = [
    "HDFCBANK.NS",
    "TCS.NS",
    "SUNPHARMA.NS",
    "MARUTI.NS",
    "HINDUNILVR.NS"
]

os.makedirs("data", exist_ok=True)

for stock in stocks:

    print(f"Downloading {stock}...")

    df = yf.download(
        stock,
        start="2021-01-01",
        end="2025-12-31",
        interval="1d",
        auto_adjust=True,
        progress=False
    )

    # Fix Yahoo Finance multi-index columns
    if hasattr(df.columns, "levels"):
        df.columns = df.columns.get_level_values(0)

    df.to_csv(f"data/{stock}.csv")

    print(f"Saved: data/{stock}.csv")
