##########################################
# accumulatescores.py
#
##########################################

# display title
print("The test score program")
print()
print("Enter three test scores")
print("==========================")

# get scores from user and accumulate the total
total_score = 0
total_score += int(input("Enter test score: "))
total_score += int(input("Enter test score: "))
total_score += int(input("Enter test score: "))

# calculate the average score
average_score = round(total_score / 3)

# format and display results
print("==========================")
print("Total Score: ", total_score,
      "\nAverage Score:", average_score)
print()
print("Bye")