import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram
import pandas as pd
import os

def generate_spectrogram():
    os.makedirs("../outputs/plots", exist_ok=True)

    df = pd.read_csv("../data/stock_data.csv")

    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df = df.dropna()

    signal = df['Close'].values.astype(float)

    f, t, Sxx = spectrogram(signal)

    plt.pcolormesh(t, f, Sxx)
    plt.title("Spectrogram")
    plt.ylabel("Frequency")
    plt.xlabel("Time")
    plt.savefig("../outputs/plots/spectrogram.png")
    plt.show()

    print("✅ Spectrogram generated!")

    return Sxx

if __name__ == "__main__":
    generate_spectrogram()