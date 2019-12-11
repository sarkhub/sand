# display the title
print("The Miles Per Gallon Program")
print()

# get input from user
miles_driven = float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))

# calculate and round miles per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg, 2)

# print the result:
print()
print("Miles Per Gallon:\t\t" + str(mpg))
print()
print("Bye")
