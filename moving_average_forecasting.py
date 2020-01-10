# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 12:56:54 2020

@author: -
"""

#######################################################################

# Moving Average Forecasting



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as pdr

stock_hist = pdr.get_data_yahoo('ORCL', start = '2015-01-01')
# get rid of Adj Close 
stock_hist = stock_hist.drop('Adj Close', axis=1)
# round to 2 decimal places
stock_hist = round(stock_hist,2)

# create 5 day average
# stock_hist['5-day'] = stock_hist['Close'].rolling(5).mean()

# print(stock_hist)

# this assumes you aready know the closing price which we do not
# so we have to use shift()
# roll forecast foward one period.
stock_hist['5-day'] = stock_hist['Close'].rolling(5).mean().shift()

# print(stock_hist)


# plot 5-day alongside close.
plt.plot(stock_hist['Close'][-120:])
plt.plot(stock_hist['5-day'][-120:])

# so we are off a little since the end of the graph does not line up

# put in error measure
# Mean Absolute Deviation
stock_hist['MAD'] = np.abs(stock_hist['Close'] - stock_hist['5-day'])

print('Mean Absolute Deviation')
print(stock_hist['MAD'].mean())
# this shows how much you are off in dollars positive or negative


# account for the scaling of the data we are using
# Mean Absolute Percent Error
stock_hist['MAPE'] = stock_hist['MAD'] / stock_hist['Close']
print('Mean Absolute Percent Error')
print(stock_hist['MAPE'].mean())



# Mean Square Error
# this resembles the variance and therefore the std dev
stock_hist['MSE'] = stock_hist['MAD'] ** 2
print('Mean Square Error')
print(stock_hist['MSE'].mean())
# This is the square as the name implies

MSE = stock_hist['MSE'].mean()


RMSE = np.sqrt(MSE)
print('Relative Mean Square Error')
print(RMSE)


# go through with 10 day and see if you get better error measures.
# rolling(5) -> rolling(10)
















