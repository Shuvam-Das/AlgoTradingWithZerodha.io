import yfinance as yf
import pandas as pd
import numpy as np

def generate_moving_average_strategy(ticker: str, short_window: int = 40, long_window: int = 100):
    """
    Generates a moving average strategy for a given ticker.
    """
    data = yf.download(ticker, period="1y", interval="1d")
    data['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    data['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
    data['signal'] = 0
    data['signal'][short_window:] = np.where(data['short_mavg'][short_window:] > data['long_mavg'][short_window:], 1, 0)
    data['positions'] = data['signal'].diff()
    return data