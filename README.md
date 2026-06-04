# AI-Driven Stock Forecasting & Portfolio Optimization

## Overview

This project presents an end-to-end stock market forecasting and portfolio optimization pipeline using historical stock data from the National Stock Exchange (NSE) of India.

The system performs data collection, preprocessing, time-series analysis, forecasting, volatility estimation, and portfolio construction. Multiple forecasting approaches are compared to identify the most suitable model for each stock.

---

## Objectives

- Forecast future stock prices using statistical and machine learning approaches.
- Compare forecasting models using evaluation metrics.
- Analyze stock volatility and risk.
- Construct a diversified investment portfolio.
- Generate actionable insights for investment decision-making.

---

## Stocks Analyzed

- HDFCBANK.NS
- TCS.NS
- SUNPHARMA.NS
- MARUTI.NS
- HINDUNILVR.NS

---

## Project Workflow

### 1. Data Collection

Historical stock price data was collected using Yahoo Finance through the `yfinance` library.

### 2. Data Preprocessing

- Missing value handling
- Date formatting
- Train-Test Split
- Stationarity checking

### 3. Exploratory Time Series Analysis

- Rolling Volatility Analysis
- STL (Seasonal-Trend Decomposition)
- Trend and Residual Analysis

### 4. Stationarity Testing

Augmented Dickey-Fuller (ADF) Test was performed on all stock series.

### 5. Forecasting Models

#### ARIMA

- Statistical forecasting model
- Used after stationarity verification
- Automatically selected optimal parameters

#### Prophet

- Developed by Meta
- Captures trend and seasonality
- Used for comparative forecasting analysis

### 6. Model Evaluation

Models were evaluated using:

- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)

### 7. Volatility Analysis

30-day rolling volatility was calculated for all stocks to estimate investment risk.

### 8. Portfolio Optimization

A virtual portfolio of ₹10,00,000 was allocated across selected stocks based on:

- Forecasting performance
- Volatility analysis
- Diversification principles

---

## Results

### Best Forecasting Model Per Stock

| Stock         | Best Model | MAPE (%) |
| ------------- | ---------- | -------- |
| HDFCBANK.NS   | ARIMA      | 1.44     |
| TCS.NS        | Prophet    | 5.89     |
| SUNPHARMA.NS  | ARIMA      | 3.54     |
| MARUTI.NS     | ARIMA      | 16.61    |
| HINDUNILVR.NS | Prophet    | 3.13     |

---

## Portfolio Allocation

| Stock         | Allocation (%) |
| ------------- | -------------- |
| HINDUNILVR.NS | 30             |
| HDFCBANK.NS   | 25             |
| SUNPHARMA.NS  | 20             |
| TCS.NS        | 15             |
| MARUTI.NS     | 10             |

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Statsmodels
- Prophet
- Scikit-learn
- yFinance

---

## Project Structure

```text
src/
│
├── data_collection.py
├── preprocessing.py
├── task1_analysis.py
├── seasonal_analysis.py
├── adf_test.py
├── arima_tcs.py
├── prophet_tcs.py
├── model_comparison.py
├── volatility_analysis.py
├── portfolio_optimization.py
└── final_summary.py
```

---

## Future Improvements

- GRU/LSTM-based forecasting
- Streamlit Dashboard Deployment
- Real-Time Market Data Integration
- Portfolio Optimization using Modern Portfolio Theory
- Sharpe Ratio-Based Allocation

---

## Author

Harsh Singh

B.Tech Computer Science & Engineering

Central University of Jammu
