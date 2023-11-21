# data_fetch.py

import yfinance as yf
from datetime import datetime, timedelta
from utils import config

def fetch_historical_data(symbol = 'USD', start_date = '2023-01-01', end_date = '2023-12-31'):
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')

    historical_data = yf.download(symbol, start=start_date, end=end_date)

    return historical_data

def fetch_live_data():
    # In a simulated environment, you might not have live data.
    # You can consider using the last row of historical data as live data.
    live_data = None  # You can modify this based on your requirements

    return live_data
