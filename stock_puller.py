# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:06:12 2020

@author: -
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as pdr

stock_hist = pdr.get_data_yahoo('ORCL', start = '2015-01-01')
# get rid of Adj Close 
stock_hist = stock_hist.drop('Adj Close', axis=1)
# round to 2 decimal places
stock_hist = round(stock_hist,2)

# print(stock_hist)

# with plt.style.context('ggplot'):
#     plt.plot(stock_hist.Close)
    
    
# resample or downsample because data is too noisy
stock_hist.index = pd.DatetimeIndex(stock_hist.index)
monthly = stock_hist.resample('BM').last()  
# last business day of month  also .first()   BM business
# M is just month sat or sun included.

print(monthly)


plt.plot(monthly['Close'])

# calculate the change from day to day.
# shift(5) = shift from last 5 days.
stock_hist['Change'] = stock_hist['Close'] - stock_hist['Close'].shift()

# print(stock_hist)
    
# not really useful because it is not scaled to the price.

# need natural log of the change
stock_hist['LN_Change'] = np.log(stock_hist['Close'] / stock_hist['Close'].shift())

# print(stock_hist)

# this is now scaled to the price and we get the instantaneous rate of return

# see how it behaves
with plt.style.context('ggplot'):
    plt.figure(figsize=(10,8))
    plt.hist(stock_hist.LN_Change[1:],bins=50, edgecolor='black', density='True')
    
    
# create volatility measure by std dev as compared to last month
# Daily Vol  volatility
stock_hist['Daily Vol'] = stock_hist['LN_Change'].rolling(21).std().shift()
# calculate expected change
stock_hist['Exp Change'] = stock_hist['Close'] * stock_hist['Daily Vol']

# print(stock_hist)

# start at 22nd row since NaN is present and not able to be calculated
stock_hist = stock_hist[22:]

print(stock_hist)





    