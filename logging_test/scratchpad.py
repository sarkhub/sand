import datetime

x = datetime.datetime.now()
print(x.strftime("%y%m%d%H%M%S%f"))
# %f is microsecond

dt_now = x.strftime("%y%m%d%H%M%S%f")

print("---------------------------")

print(dt_now)