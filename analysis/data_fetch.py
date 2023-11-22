# data_fetch.py

import yfinance as yf


def fetch_historical_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data.reset_index()
