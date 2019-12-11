###########################################
#
# stockfileloader
#
# procedural way to load multiple files
#
###########################################

import os
import pandas as pd
os.chdir('C:\PANDAS2019\pandas_tutorial_jupyter_output\data')
os.getcwd()

def check_files():
    print("Checking for files")

def load_files(name):
    print("name -> ", name)

def main():

    print("Starting stockfileloader routine")

    check_files()

    load_files('AAPL')

    print("Complete!")









if __name__ == "__main__":
    main()