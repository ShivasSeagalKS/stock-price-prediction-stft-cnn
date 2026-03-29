import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_frequency():
    os.makedirs("../outputs/plots", exist_ok=True)

    df = pd.read_csv("../data/stock_data.csv")

    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df = df.dropna()

    signal = df['Close'].values.astype(float)

    fft = np.fft.fft(signal)
    freq = np.fft.fftfreq(len(signal))

    plt.plot(freq, np.abs(fft))
    plt.title("Frequency Spectrum")
    plt.savefig("../outputs/plots/frequency.png")
    plt.show()

    print("✅ Frequency spectrum saved!")

if __name__ == "__main__":
    plot_frequency()