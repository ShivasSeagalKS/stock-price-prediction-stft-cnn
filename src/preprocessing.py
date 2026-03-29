import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_and_preprocess():
    df = pd.read_csv("../data/stock_data.csv")

    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df = df.dropna()

    values = df['Close'].values.reshape(-1, 1)

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(values)

    print("✅ Data preprocessed!")

    return scaled, scaler

if __name__ == "__main__":
    load_and_preprocess()