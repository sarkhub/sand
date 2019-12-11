###########################################
#
# randomtest
#
# testing modules for random
# number generation
#
###########################################

import random


# the use of random method
print("Using random float")
number = random.random()                 # a float value >= 0.0 and < 1.0
print(number)

number = random.random() * 100           # a float value >= 0.0 and < 100
print(number)
number = round(number, 2)                # round number to two decimal places
print(number)

# the use of randint method
print("Using randint")
number = random.randint(1, 100)          # an int from 1 to 100
print(number)
number = random.randint(101, 200)        # an int from 101 to 200
print(number)
number = random.randint(0, 7)            # an int from 0 to 7
print(number)

# the use of randrange method
print("Using randrange")
number = random.randrange(1, 100)        # an int from 1 to 99
print(number)
number = random.randrange(100, 200, 2)   # an even int from 100 to 198
print(number)
number = random.randrange(11, 250, 2)    # an odd int from 11 to 249
print(number)

# simulate rolling a pair of dice
print("Roll dice")
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
print("Your roll: ", die1, die2)

