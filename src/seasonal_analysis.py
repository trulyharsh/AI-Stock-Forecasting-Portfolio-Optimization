import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import STL

stocks = [
    "HDFCBANK.NS",
    "TCS.NS",
    "SUNPHARMA.NS",
    "MARUTI.NS",
    "HINDUNILVR.NS"
]

for stock in stocks:

    df = pd.read_csv(f"data/{stock}.csv")

    df["Date"] = pd.to_datetime(df["Date"])

    df.set_index("Date", inplace=True)

    stl = STL(
        df["Close"],
        period=252
    )

    result = stl.fit()

    fig = result.plot()

    fig.set_size_inches(12, 8)

    plt.suptitle(
        f"{stock} STL Decomposition",
        fontsize=14
    )

    plt.savefig(
        f"outputs/plots/{stock}_stl.png"
    )

    plt.close()

    print(f"Saved STL plot for {stock}")
