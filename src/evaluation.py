from sklearn.metrics import mean_squared_error
import numpy as np

def evaluate():
    y_true = np.array([1.0])
    y_pred = np.array([0.8])

    mse = mean_squared_error(y_true, y_pred)
    print("MSE:", mse)

if __name__ == "__main__":
    evaluate()