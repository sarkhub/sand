import os
import csv
import time

os.chdir(r"/home/dbsand/sand/dat/")

with open('listings.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['TICKER'])
        print('wait event')
        time.sleep(10)  # seconds
        