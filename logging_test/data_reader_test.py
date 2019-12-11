import os
import datetime
import pandas as pd


x = datetime.datetime.now()
dt_now = x.strftime("%y%m%d%H%M%S%f")
ext = '.txt'
file_nm = 'data_reader_test'



def init_log():

    os.chdir('C:\PANDAS2019\logs')
    log_msg = 'Application '+file_nm+' run at '+dt_now
    file_object = open(dt_now+file_nm+ext, 'w')
    file_object.write(log_msg)
    file_object.close()

def log_append(log_msg_append):

    os.chdir('C:\PANDAS2019\logs')
    file_object = open(dt_now + file_nm + ext, 'a')
    file_object.write('\n')
    file_object.write(log_msg_append)
    file_object.close()


# --------------------------------------------------------
# -- main
init_log()


# --------------------------------------------------------
# -- read data and display results
os.chdir('C:\PANDAS\practicaltimeseries\data')
print('X')
sp500_df = pd.read_csv('GSPC.csv')

# change the row indices of the dataframe using the Date column
sp500_df.index = sp500_df['Date']

print(sp500_df.head(10))



# -- log results
log_append('sp500 top 10 Close:')
log_append(pd.Series.to_string(sp500_df['Close'].head(10)))




log_append('completed process')

