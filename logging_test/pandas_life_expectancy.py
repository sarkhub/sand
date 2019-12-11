import os
import datetime
import pandas as pd

x = datetime.datetime.now()
dt_now = x.strftime("%y%m%d%H%M%S%f")
ext = '.txt'
file_nm = 'pandas_life_expectancy'



os.chdir('C:\PANDAS2019\logs')
log_msg = 'Application '+file_nm+' run at '+dt_now
file_object = open(dt_now+file_nm+ext, 'w')
file_object.write(log_msg)
file_object.close()

def log_append(log_msg_append):
    file_object = open(dt_now + file_nm + ext, 'a')
    file_object.write('\n')
    file_object.write(log_msg_append)
    file_object.close()

# ------------------------------------------------------------
# -- Load file for analysis
log_append('Load file for analysis')

df = pd.read_csv('C:\PANDAS\CH10\data\gapminder.tsv', sep='\t')

print(df.head())

# calculate the average life expectancy for each year
avg_life_exp_by_year = df.groupby('year').lifeExp.mean()
print(avg_life_exp_by_year)
log_append('Results of average life expectancy by year:')
log_append(pd.Series.to_string(avg_life_exp_by_year))
# -- END Load file for analysis


log_append('success!')

print('Exit '+file_nm)