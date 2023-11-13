import pandas as pd
import numpy as np

def SMA(data, period=30, column='Close'):
    return data[column].rolling(window=period).mean()

def EMA(data, period=20, column='Close'):
    return data[column].ewm(span=period, adjust=False).mean()

def MACD(data, period_long=26, period_short=12, period_signal=9, column='Close'):
    shortEMA = EMA(data, period_short, column=column)
    longEMA = EMA(data, period_long, column=column)
    data['MACD'] = shortEMA - longEMA
    data['Signal_Line'] = EMA(data, period_signal, column='MACD')
    return data


def RSI(data, period=14, column='Close'):
    delta = data[column].diff(1)
    delta = delta[1:]
    up = delta.copy()
    down = delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    data['up'] = up
    data['down'] = down
    AVG_Gain = SMA(data, period, column='up')
    AVG_Loss = abs(SMA(data, period, column='down'))
    RS = AVG_Gain / AVG_Loss
    RSI = 100.0 - (100.0 / (1.0 + RS))
    data['RSI'] = RSI
    return data

def VWAP(data):
    typical_price = (data['High'] + data['Low'] + data['Close']) / 3
    data['Typical_Price'] = typical_price
    data['Typical_Price_Volume'] = typical_price * data['Volume']
    data['VWAP'] = data['Typical_Price_Volume'].cumsum() / data['Volume'].cumsum()
    return data

def OBV(data):
    data['OBV'] = np.where(data['Close'] > data['Close'].shift(1), data['Volume'], np.where(data['Close'] < data['Close'].shift(1), -data['Volume'], 0)).cumsum()
    return data

def ATR(data, period=14):
    high_low = data['High'] - data['Low']
    high_close = abs(data['High'] - data['Close'].shift(1))
    low_close = abs(data['Low'] - data['Close'].shift(1))
    ranges = pd.concat([high_low, high_close, low_close], axis=1)
    true_range = np.max(ranges, axis=1)
    data['ATR'] = true_range.rolling(period).mean()
    return data

def Bollinger_Bands(data, period=20, column='Close'):
    data['SMA'] = SMA(data, period=period, column=column)
    data['STD'] = data[column].rolling(window=period).std()
    data['Upper_Band'] = data['SMA'] + (data['STD'] * 2)
    data['Lower_Band'] = data['SMA'] - (data['STD'] * 2)
    data = data.dropna()
    return data

def Pivots(data):
    data['Pivot_Point'] = (data['High'] + data['Low'] + data['Close']) / 3
    data['R1'] = (2 * data['Pivot_Point']) - data['Low']
    data['S1'] = (2 * data['Pivot_Point']) - data['High']
    data['R2'] = data['Pivot_Point'] + (data['High'] - data['Low'])
    data['S2'] = data['Pivot_Point'] - (data['High'] - data['Low'])
    data['R3'] = data['High'] + 2 * (data['Pivot_Point'] - data['Low'])
    data['S3'] = data['Low'] - 2 * (data['High'] - data['Pivot_Point'])
    return data

def Stochastic_Oscillator(data, period=14):
    data['%K'] = ((data['Close'] - data['Low'].rolling(period).min()) / (data['High'].rolling(period).max() - data['Low'].rolling(period).min())) * 100
    data['%D'] = data['%K'].rolling(3).mean()
    return data

def Williams_R(data, period=14):
    data['%R'] = ((data['High'].rolling(period).max() - data['Close']) / (data['High'].rolling(period).max() - data['Low'].rolling(period).min())) * -100
    return data

def Aroon(data, period=25):
    data['Aroon_Up'] = ((period - data['High'].rolling(period).apply(lambda x: x.argmax(), raw=True)) / period) * 100
    data['Aroon_Down'] = ((period - data['Low'].rolling(period).apply(lambda x: x.argmin(), raw=True)) / period) * 100
    return data

def ADX(data, period=14):
    data['UpMove'] = data['High'] - data['High'].shift(1)
    data['DownMove'] = data['Low'].shift(1) - data['Low']
    data['Zero'] = 0
    data['Plus_DM'] = np.where((data['UpMove'] > data['DownMove']) & (data['UpMove'] > data['Zero']), data['UpMove'], 0)
    data['Minus_DM'] = np.where((data['DownMove'] > data['UpMove']) & (data['DownMove'] > data['Zero']), data['DownMove'], 0)
    data['Plus_DI'] = (100 * (data['Plus_DM'].rolling(period).mean() / data['ATR']))
    data['Minus_DI'] = (100 * (data['Minus_DM'].rolling(period).mean() / data['ATR']))
    data['DX'] = (100 * (abs(data['Plus_DI'] - data['Minus_DI']) / (data['Plus_DI'] + data['Minus_DI'])))
    data['ADX'] = data['DX'].rolling(period).mean()
    return data

def Ichimoku_Cloud(data):
    data['Tenkan_Sen'] = (data['High'].rolling(9).max() + data['Low'].rolling(9).min()) / 2
    data['Kijun_Sen'] = (data['High'].rolling(26).max() + data['Low'].rolling(26).min()) / 2
    data['Senkou_Span_A'] = ((data['Tenkan_Sen'] + data['Kijun_Sen']) / 2).shift(26)
    data['Senkou_Span_B'] = ((data['High'].rolling(52).max() + data['Low'].rolling(52).min()) / 2).shift(26)
    data['Chikou_Span'] = data['Close'].shift(-26)
    return data

def Chaikin_Oscillator(data):
    data['Money_Flow_Multiplier'] = ((data['Close'] - data['Low']) - (data['High'] - data['Close'])) / (data['High'] - data['Low'])
    data['Money_Flow_Volume'] = data['Money_Flow_Multiplier'] * data['Volume']
    data['ADL'] = data['Money_Flow_Volume'].cumsum()
    data['3_EMA'] = EMA(data, period=3, column='ADL')
    data['10_EMA'] = EMA(data, period=10, column='ADL')
    data['Chaikin_Oscillator'] = data['3_EMA'] - data['10_EMA']
    return data

def CCI(data, period=20):
    data['TP'] = (data['High'] + data['Low'] + data['Close']) / 3
    data['CCI'] = (data['TP'] - data['TP'].rolling(period).mean()) / (0.015 * data['TP'].rolling(period).std())
    return data

def EOM(data, period=14):
    distance_moved = ((data['High'] + data['Low']) / 2) - ((data['High'].shift(1) + data['Low'].shift(1)) / 2)
    box_ratio = (data['Volume'] / 100000000) / (data['High'] - data['Low'])
    data['EOM'] = distance_moved / box_ratio
    data['EOM_MA'] = data['EOM'].rolling(period).mean()
    return data

def Force_Index(data, period=13):
    data['Force_Index'] = data['Close'].diff(period) * data['Volume'].diff(period)
    return data

def KST_Oscillator(data, r1=10, r2=15, r3=20, r4=30, n1=10, n2=10, n3=10, n4=15):
    rocma1 = ((data['Close'] / data['Close'].shift(r1)) - 1).rolling(n1).mean()
    rocma2 = ((data['Close'] / data['Close'].shift(r2)) - 1).rolling(n2).mean()
    rocma3 = ((data['Close'] / data['Close'].shift(r3)) - 1).rolling(n3).mean()
    rocma4 = ((data['Close'] / data['Close'].shift(r4)) - 1).rolling(n4).mean()
    data['KSTO'] = (rocma1 * 1) + (rocma2 * 2) + (rocma3 * 3) + (rocma4 * 4)
    return data

def KST_Signal_Line(data, r1=10, r2=15, r3=20, r4=30, n1=10, n2=10, n3=10, n4=15, sn=9):
    rocma1 = ((data['Close'] / data['Close'].shift(r1)) - 1).rolling(n1).mean()
    rocma2 = ((data['Close'] / data['Close'].shift(r2)) - 1).rolling(n2).mean()
    rocma3 = ((data['Close'] / data['Close'].shift(r3)) - 1).rolling(n3).mean()
    rocma4 = ((data['Close'] / data['Close'].shift(r4)) - 1).rolling(n4).mean()
    data['KST_Signal_Line'] = ((rocma1 * 1) + (rocma2 * 2) + (rocma3 * 3) + (rocma4 * 4)).rolling(sn).mean()
    return data

def KST_Diff(data, r1=10, r2=15, r3=20, r4=30, n1=10, n2=10, n3=10, n4=15, sn=9):
    rocma1 = ((data['Close'] / data['Close'].shift(r1)) - 1).rolling(n1).mean()
    rocma2 = ((data['Close'] / data['Close'].shift(r2)) - 1).rolling(n2).mean()
    rocma3 = ((data['Close'] / data['Close'].shift(r3)) - 1).rolling(n3).mean()
    rocma4 = ((data['Close'] / data['Close'].shift(r4)) - 1).rolling(n4).mean()
    data['KST_Diff'] = ((rocma1 * 1) + (rocma2 * 2) + (rocma3 * 3) + (rocma4 * 4)) - ((rocma1 * 1) + (rocma2 * 2) + (rocma3 * 3) + (rocma4 * 4)).rolling(sn).mean()
    return data

    