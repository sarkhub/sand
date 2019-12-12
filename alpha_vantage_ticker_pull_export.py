from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
#from matplotlib.pyplot import figure
#import matplotlib.pyplot as plt
import pandas as pd

# Your key here
key = 'key'
# Chose your output format, or default to JSON (python dict)
ts = TimeSeries(key, output_format='pandas')
ti = TechIndicators(key)

# Get the data, returns a tuple
# aapl_data is a pandas dataframe, aapl_meta_data is a dict
tick_data, tick_meta_data = ts.get_daily(symbol='ORCL')




# Visualization
#figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
#tick_data['4. close'].plot()
#plt.tight_layout()
#plt.grid()
#plt.show()


# convert dict to dataframe
stock_df = pd.DataFrame.from_dict(tick_data)

# add symbol column and poplulate
stock_df['symbol'] = 'ORCL'

# see contents with new column and ticker symbol
#stock_df

# export to csv
export_csv = stock_df.to_csv (r'C:\tmp\export_dataframe.csv', index = True, header=True) 
