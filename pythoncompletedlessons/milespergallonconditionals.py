##########################################
# milespergallonconditionals.py
#
##########################################

# display welcome message
print("Miles per gallon")
print()

# get input
miles_driven = float(input("Enter miles driven:  "))
gallons_used = float(input("Enter gallons of gas used:   "))

if miles_driven > 0 and gallons_used > 0:
    mpg = round((miles_driven / gallons_used), 2)
    print("Miles Per Gallon:     ", mpg)
else:
    print("Both entries must be greater than zero")