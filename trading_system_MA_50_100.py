# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 14:30:07 2020

@author: -
"""
###############################################################
## Trading System simple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as pdr


stock_hist = pdr.get_data_yahoo('ORCL', start = '2019-06-01')
# get rid of Adj Close 
stock_hist = stock_hist.drop('Adj Close', axis=1)
# round to 2 decimal places
stock_hist = round(stock_hist,2)


stock_hist['50-day'] = stock_hist['Close'].rolling(50).mean()
stock_hist['100-day'] = stock_hist['Close'].rolling(100).mean()
stock_hist['Change'] = np.log(stock_hist.Close / stock_hist.Close.shift())


# print(stock_hist)


# when faster signal moves above slower = signal to buy

# when slower signal moves above faster = signal to sell short

with plt.style.context('ggplot'):
    plt.figure(figsize=(8,6))
    plt.plot(stock_hist.Close[-120:])
    plt.plot(stock_hist['50-day'][-120:])
    plt.plot(stock_hist['100-day'][-120:])
    plt.legend(loc=2)
    
    # this does not take in account equality
stock_hist['position'] = np.where(stock_hist['50-day'] > stock_hist['100-day'], 1, 0)
stock_hist['position'] = np.where(stock_hist['50-day'] <= stock_hist['100-day'] , -1, stock_hist['position'])

print(stock_hist['position'])

# capture the return
stock_hist['system'] = stock_hist['position'] * stock_hist['Change']


# plot
stock_hist[['Change', 'system']].cumsum().plot()



