

###########################################
#
# stockfileloader
#
# procedural way to load multiple files
#
###########################################

import os
import pandas as pd



 


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

        x = currStock["Date"]
        y = currStock["Close"]
        # plotting the points  
        plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3 
             #, marker='o'
             , markerfacecolor='blue', markersize=12) 
  
        # setting x and y axis range 
        plt.ylim(1,200) 
        plt.xlim(1,200) 
  
        # naming the x axis 
        plt.xlabel('x - axis') 
        # naming the y axis 
        plt.ylabel('y - axis') 
  
        # giving a title to my graph 
        plt.title(stockname) 
  
        # function to show the plot 
        plt.show() 
    

def main():

    print("Starting stockfileloader routine")

    check_files()

    
    
    
    

    print("Complete!")



if __name__ == "__main__":
    main()
    