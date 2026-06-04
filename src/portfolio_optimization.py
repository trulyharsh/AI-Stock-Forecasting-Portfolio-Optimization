import pandas as pd

capital = 1000000

allocation = {
    "HINDUNILVR.NS": 0.30,
    "HDFCBANK.NS": 0.25,
    "SUNPHARMA.NS": 0.20,
    "TCS.NS": 0.15,
    "MARUTI.NS": 0.10
}

results = []

for stock, weight in allocation.items():

    df = pd.read_csv(
        f"data/{stock}.csv"
    )

    latest_price = df["Close"].iloc[-1]

    amount = capital * weight

    shares = int(
        amount / latest_price
    )

    invested = (
        shares * latest_price
    )

    results.append([
        stock,
        round(weight * 100, 2),
        round(latest_price, 2),
        shares,
        round(invested, 2)
    ])

portfolio = pd.DataFrame(
    results,
    columns=[
        "Stock",
        "Allocation (%)",
        "Latest Price",
        "Shares",
        "Investment"
    ]
)

portfolio.to_csv(
    "outputs/reports/portfolio_allocation.csv",
    index=False
)

print(portfolio)

print(
    "\nTotal Investment:",
    round(
        portfolio["Investment"].sum(),
        2
    )
)
