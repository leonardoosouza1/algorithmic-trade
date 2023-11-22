# trend_analysis.py

import pandas as pd
import numpy as np
import ta


def analyze_trend(data):
    # Calculate moving averages
    data['MA_Short'] = ta.trend.sma_indicator(data['Close'], window=5)
    data['MA_Long'] = ta.trend.sma_indicator(data['Close'], window=20)

    # Create buy/sell signals based on moving average crossover
    data['Signal'] = 0  # Hold signal by default
    data.loc[data['MA_Short'] > data['MA_Long'], 'Signal'] = 1  # Buy signal
    data.loc[data['MA_Short'] < data['MA_Long'], 'Signal'] = -1  # Sell signal

    return data
