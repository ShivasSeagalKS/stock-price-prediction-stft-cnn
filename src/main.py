from data_collection import fetch_stock_data
from preprocessing import load_and_preprocess
from spectrogram import generate_spectrogram
from model import train_model

# Step 1: Collect data
fetch_stock_data()

# Step 2: Preprocess
data, scaler = load_and_preprocess()

# Step 3: Generate spectrogram
Sxx = generate_spectrogram()

# Step 4: Prepare input
import numpy as np
X = np.expand_dims(Sxx, axis=-1)
X = np.expand_dims(X, axis=0)

y = np.array([0.5])  # dummy target

# Step 5: Train model
model = train_model(X, y)