

###########################################
#
# plottester
#
# procedural way to load multiple files
#
###########################################

import os
import pandas as pd



 
def generate_plot(x, y, partner_name):
    import matplotlib.pyplot as plt 
  
   
  
    # plotting the points  
    plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, 
             marker='o', markerfacecolor='blue', markersize=12) 
  
    # setting x and y axis range 
    plt.ylim(1,20) 
    plt.xlim(1,20) 
  
    # naming the x axis 
    plt.xlabel('x - axis') 
    # naming the y axis 
    plt.ylabel('y - axis') 
  
    # giving a title to my graph 
    plt.title(partner_name) 
  
    # function to show the plot 
    plt.show() 




def main():

    print("Starting plottester routine")
    
     # x axis values 
    x = [1,2,3,4,5,6] 
    # corresponding y axis values 
    y = [2,4,1,5,2,6] 
    
    partner_name = 'Infocon'

    generate_plot(x, y, partner_name)
    
    
         # x axis values 
    x = [12,10,10,14,18,7] 
    # corresponding y axis values 
    y = [12,14,11,15,20,16] 
    
    partner_name = 'Indiana'

    generate_plot(x, y, partner_name)

    
    
    
    

    print("Complete!")



if __name__ == "__main__":
    main()
    