import yfinance as yf
import pandas as pd
import os

def fetch_stock_data():
    os.makedirs("../data", exist_ok=True)

    data = yf.download("AAPL", start="2015-01-01", end="2023-01-01")

    data = data[['Close']]
    data.reset_index(drop=True, inplace=True)

    data.to_csv("../data/stock_data.csv", index=False)

    print("✅ Data collected and saved!")

if __name__ == "__main__":
    fetch_stock_data()