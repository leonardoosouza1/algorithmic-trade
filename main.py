import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import Indicators.main as ind

selected_period = "10y"

def main():
    usd_eur = yf.Ticker("USDEUR=X")
    hist = usd_eur.history(period=selected_period)
    
    hist_SMA = ind.SMA(hist)
    hist_EMA = ind.EMA(hist)
    hist_MACD = ind.MACD(hist)
    hist_RSI = ind.RSI(hist)
    hist_VWAP = ind.VWAP(hist)
    hist_OBV = ind.OBV(hist)
    hist_ATR = ind.ATR(hist)
    hist_BB = ind.Bollinger_Bands(hist)
    hist_PVP = ind.Pivots(hist)
    hist_Stochastic_Oscillator = ind.Stochastic_Oscillator(hist)
    hist_WR = ind.Williams_R(hist)
    hist_AR = ind.Aroon(hist)
    hist_ADX = ind.ADX(hist)
    hist_CCI = ind.CCI(hist)
    hist_CHO = ind.Chaikin_Oscillator(hist)
    hist_CCI = ind.CCI(hist)
    hist_EOM= ind.EOM(hist)
    hist_FCI = ind.Force_Index(hist)
    hist_KSTO = ind.KST_Oscillator(hist)
    hist_KSTSL = ind.KST_Signal_Line(hist)
    hist_KSTDIFF = ind.KST_Diff(hist)

    graph = pd.DataFrame()
    graph['PRICE'] = hist['Close']
    graph['SMA'] = hist_SMA
    graph['EMA'] = hist_EMA
    graph['MACD'] = hist_MACD['MACD']
    #graph['RSI'] = hist_RSI['RSI']
    graph['VWAP'] = hist_VWAP['VWAP']
    graph['OBV'] = hist_OBV['OBV']
    graph['ATR'] = hist_ATR['ATR']
    graph['Upper_Band'] = hist_BB['Upper_Band']
    graph['Lower_Band'] = hist_BB['Lower_Band']
    graph['Pivot_Point'] = hist_PVP['Pivot_Point']
    #graph['R1'] = hist_PVP['R1']
    #graph['S1'] = hist_PVP['S1']
    #graph['R2'] = hist_PVP['R2']
    #graph['S2'] = hist_PVP['S2']
    #graph['R3'] = hist_PVP['R3']
    #graph['S3'] = hist_PVP['S3']
    #graph['%K'] = hist_Stochastic_Oscillator['%K']
    #graph['%D'] = hist_Stochastic_Oscillator['%D']
    #graph['%R'] = hist_WR['%R']
    #graph['Aroon_Up'] = hist_AR['Aroon_Up']
    #graph['Aroon_Down'] = hist_AR['Aroon_Down']
    #graph['ADX'] = hist_ADX['ADX']
    #graph['CCI'] = hist_CCI['CCI']
    #graph['CHO'] = hist_CHO['Chaikin_Oscillator']
    #graph['EOM'] = hist_EOM['EOM']
    #graph['FCI'] = hist_FCI['Force_Index']
    #graph['KSTO'] = hist_KSTO['KSTO']
    #graph['KSTSL'] = hist_KSTSL['KST_Signal_Line']
    #graph['KSTDIFF'] = hist_KSTDIFF['KST_Diff']
   
    

    graph.plot()
    plt.show()

    



if __name__ == "__main__":

    main()
