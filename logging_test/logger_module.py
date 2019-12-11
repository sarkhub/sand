import os
import datetime

x = datetime.datetime.now()
dt_now = x.strftime("%y%m%d%H%M%S%f")
ext = '.txt'
file_nm = 'logger_module'

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

log_append('new appended message')

log_append('success!')

print('Exit '+file_nm)