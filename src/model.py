import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense
import os
from spectrogram import generate_spectrogram

def train_model():
    os.makedirs("../outputs/model", exist_ok=True)

    # Get spectrogram
    Sxx = generate_spectrogram()

    # Prepare input
    X = np.expand_dims(Sxx, axis=-1)
    X = np.expand_dims(X, axis=0)

    y = np.array([0.5])  # dummy target

    model = Sequential([
        Conv2D(32, (3,3), activation='relu', input_shape=X.shape[1:]),
        Flatten(),
        Dense(50, activation='relu'),
        Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse')

    model.fit(X, y, epochs=5)

    model.save("../outputs/model/model.h5")

    print("✅ Model trained and saved!")

if __name__ == "__main__":
    train_model()