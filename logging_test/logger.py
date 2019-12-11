import os
import datetime

x = datetime.datetime.now()
dt_now = x.strftime("%y%m%d%H%M%S%f")
file_nm = 'logger.txt'

os.chdir('C:\PANDAS2019\logs')
log_msg = 'this is the log from the application'
file_object = open(dt_now+file_nm, 'w')
file_object.write(log_msg)
file_object.close()