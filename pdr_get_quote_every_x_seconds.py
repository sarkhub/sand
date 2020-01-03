# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 13:51:10 2020

@author:  
"""

import pandas as pd
import pandas_datareader as pdr
from time import sleep

symbols = "AAPL ORCL MJ".split()

def get_prices(symbols):
    symbols.sort()
    return pdr.get_quote_yahoo(symbols)['price']


def main():
    while True:
        print(get_prices(symbols))
        print("CTRL + C to quit")
        sleep(5)
        

if __name__ == "__main__":
    main()
    
