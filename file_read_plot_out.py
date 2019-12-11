


import os
import pandas as pd
import matplotlib.pyplot as plt



 


FILEDIR = 'C:\PANDAS2019\pandas_tutorial_jupyter_output\data'


def check_files():
    print("Checking for files")
    for file in os.listdir(FILEDIR):
            if file.endswith(".csv"):
                    # print(file)
                    # stock_name=file.replace(".csv","")
                    # print(stock_name)
                    # stock_name = pd.read_csv(file, index_col=0, parse_dates=True)
                    # stock_name
                    load_files(file)
                    

def load_files(file):
    print("file -> ", file)
    
    os.chdir(FILEDIR)
    currStock = pd.read_csv(file)
    
    stockname=file.replace(".csv","")
    print("Loaded -> ", stockname)
    
    
    # print(currStock)      # DEBUG show contents
    plot_files(currStock, stockname)

    


def plot_files(currStock, stockname):
        print("plotting -> ", stockname)
        print()
        print(currStock.shape)
        #currStock.legend(label=stockname)
        currStock["Close"].plot(grid = True, legend=True) # Plot the adjusted closing price of current stock
        
        ######
        currStock.index = currStock['Date']

        print(currStock.head(10))


        os.chdir('C:\PANDAS2019\plots_out')
        plt.figure(figsize=(5.5, 5.5))
        currStock['Close'].plot(color='b')
        plt.title(stockname)
        plt.xlabel('Time')
        plt.ylabel('Closing Value')
        plt.savefig(stockname+'.png', format='png', dpi=300)

        ######

        return
    

def main():

    print("Starting stockfileloader routine")

    check_files()

    
    
    
    

    print("Complete!")



if __name__ == "__main__":
    main()
    