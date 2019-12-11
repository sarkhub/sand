import os
import datetime
import pandas as pd

x = datetime.datetime.now()
dt_now = x.strftime("%y%m%d%H%M%S%f")
ext = '.txt'
file_nm = 'logger_module2'

os.chdir('C:\PANDAS2019\logs')

def init_log():

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
# -- Check for files
# -- checks downloads dir for new downloaded file(s)
def check_for_files():

        for file in os.listdir('C:\PANDAS\practicaltimeseries\data'):
            if file.endswith(".csv"):
                print(file)





# ------------------------------------------------------------
# -- main
init_log()
log_append('main')
log_append('Checking for file(s)')
check_for_files()




# ------------------------------------------------------------
# -- Load file(s) for analysis



log_append('success!')

print('Exit '+file_nm)