import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_time_series():
    os.makedirs("../outputs/plots", exist_ok=True)

    df = pd.read_csv("../data/stock_data.csv")

    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df = df.dropna()

    plt.figure()
    plt.plot(df['Close'])
    plt.title("Stock Price vs Time")

    plt.savefig("../outputs/plots/time_series.png")

    print("✅ Time series plot saved!")

    plt.show()

if __name__ == "__main__":
    plot_time_series()