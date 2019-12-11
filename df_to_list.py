
import matplotlib.pyplot as plt 
from pandas import DataFrame

Products = {'Product': ['Tablet','iPhone','Laptop','Monitor'],
            'Price': [250,800,1200,300]
            }

df = DataFrame(Products, columns= ['Product', 'Price'])

Products_list = df.values.tolist()
print (Products_list)

print(df.Price)

x = df.Product
y = df.Price

# plotting the points  
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=12) 
  
# setting x and y axis range 
plt.ylim(1,2000) 
plt.xlim(1,2000) 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title(partner_name) 
  
# function to show the plot 
plt.show() 