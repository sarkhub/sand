import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir('C:\PANDAS\practicaltimeseries\data')
os.getcwd()

sp500_df = pd.read_csv('GSPC.csv')

# Change the row indices of the dataframe using the Date column
sp500_df.index = sp500_df['Date']

print(sp500_df.head(10))


os.chdir('C:\PANDAS2019\plots_out')
plt.figure(figsize=(5.5, 5.5))
sp500_df['Close'].plot(color='b')
plt.title('S&P 500 between 2001 - 2018')
plt.xlabel('Time')
plt.ylabel('Closing Value')
plt.savefig('sp500_testrun.png', format='png', dpi=300)


