import pandas as pd

# Load reports
models = pd.read_csv(
    "outputs/reports/model_results.csv"
)

volatility = pd.read_csv(
    "outputs/reports/volatility_results.csv"
)

portfolio = pd.read_csv(
    "outputs/reports/portfolio_allocation.csv"
)

# Select best model per stock
best_models = []

for stock in models["Stock"].unique():

    stock_df = models[
        models["Stock"] == stock
    ]

    best = stock_df.loc[
        stock_df["MAPE"].idxmin()
    ]

    best_models.append(best)

best_models = pd.DataFrame(best_models)

# Merge all reports
summary = best_models.merge(
    volatility,
    on="Stock"
)

summary = summary.merge(
    portfolio[
        [
            "Stock",
            "Allocation (%)",
            "Investment"
        ]
    ],
    on="Stock"
)

summary = summary[
    [
        "Stock",
        "Model",
        "RMSE",
        "MAPE",
        "Average_Volatility",
        "Allocation (%)",
        "Investment"
    ]
]

summary.to_csv(
    "outputs/reports/final_summary.csv",
    index=False
)

print(summary)
