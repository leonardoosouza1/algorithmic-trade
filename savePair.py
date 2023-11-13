import yfinance as yf

def save():
    pair = 'EURUSD=X'
    period = '10y'
    data = yf.download(pair, period=period)
    data.to_csv('data2.csv')
    print(data)


if __name__ == "__main__":
    save()