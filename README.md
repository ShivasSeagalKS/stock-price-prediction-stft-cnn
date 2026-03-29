# 📈 Stock Price Prediction using STFT and CNN

## 👤 Student Details

**Name:** Shivas Seagal K S

**Register Number:** TCR24CS061 

---

## 🎯 Objective

The objective of this project is to analyze financial time series data using signal processing techniques and predict stock prices using a Convolutional Neural Network (CNN). The project combines time–frequency analysis with deep learning for better pattern recognition.

---

## 📊 Problem Description

Financial time series data such as stock prices are non-stationary in nature. To better analyze such data, we transform it into a time–frequency domain using Short-Time Fourier Transform (STFT). The resulting spectrogram is treated as an image and fed into a CNN model for prediction.

---

## ⚙️ Methodology

### 1. Data Collection

* Stock data is collected using Yahoo Finance API
* Example: Apple Inc. (AAPL)

### 2. Data Preprocessing

* Extracted closing prices
* Converted to numeric format
* Removed missing or invalid values
* Normalized using MinMaxScaler

### 3. Signal Processing

* Applied Fourier Transform (FFT) to analyze frequency components
* Generated spectrogram using Short-Time Fourier Transform (STFT)

### 4. Visualization

* Time Series Plot (Price vs Time)
* Frequency Spectrum
* Spectrogram (Time-Frequency Representation)

### 5. Model Development

* Built a Convolutional Neural Network (CNN)
* Input: Spectrogram images
* Output: Predicted stock price

### 6. Evaluation

* Model evaluated using Mean Squared Error (MSE)

---

## 🖥️ Project Structure

```
stock-price-prediction-stft-cnn/
├── data/
├── outputs/
│   ├── plots/
│   └── model/
├── src/
├── README.md
├── requirements.txt
```

---

## ▶️ How to Run the Project

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Navigate to source folder:

```
cd src
```

3. Run files in order:

```
python data_collection.py
python preprocessing.py
python visualization.py
python frequency_spectrum.py
python spectrogram.py
python model.py
python evaluation.py
```

---

## 📂 Outputs

### ✔ Plots Generated

* Time Series Plot
* Frequency Spectrum
* Spectrogram

### ✔ Model

* Trained CNN model saved as `.h5` file

---

## 📚 References

1. Stock Market Prediction Using Deep Learning – IEEE
2. Deep Learning for Financial Time Series Forecasting
3. LSTM Networks – Hochreiter & Schmidhuber

---

## ✅ Conclusion

This project demonstrates that:

* Financial time series can be analyzed as signals
* Spectrograms help reveal hidden patterns
* CNN models can learn from time–frequency representations for prediction

---
