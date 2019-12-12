from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
#from matplotlib.pyplot import figure
#import matplotlib.pyplot as plt
import pandas as pd
import os 

os.chdir(r"C:\tmp")

# Your key here
key = 'key'


# ticker we are wanting to capture data on
ticker_symbol = 'BRK.B'


# Chose your output format, or default to JSON (python dict)
ts = TimeSeries(key, output_format='pandas')
ti = TechIndicators(key)

# Get the data, returns a tuple
# aapl_data is a pandas dataframe, aapl_meta_data is a dict
tick_data, tick_meta_data = ts.get_daily(symbol=ticker_symbol)




# Visualization
#figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
#tick_data['4. close'].plot()
#plt.tight_layout()
#plt.grid()
#plt.show()


# convert dict to dataframe
stock_df = pd.DataFrame.from_dict(tick_data)

# add symbol column and poplulate
stock_df['symbol'] = ticker_symbol

# see contents with new column and ticker symbol
#stock_df

# export to csv
export_csv = stock_df.to_csv (r'file_out.csv', index = True, header=True) 

# replace '.' in name so file does not have two '.'
ticker_symbol = ticker_symbol.replace(".","")
# change generic file name to that of the ticker
os.rename('file_out.csv', ticker_symbol+'.csv')
