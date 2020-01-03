# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 13:51:10 2020

@author:  
"""

import pandas as pd
import pandas_datareader as pdr

print(pdr.get_quote_yahoo("AAPL")['price'])



