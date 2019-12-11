###########################################
#
# listexamples
#
# working with list
#
# random is used for shuffle() and choice()
###########################################

import random

def main():




    # how to use the count(), reverse() and sort() methods
    numlist = [5, 15, 84, 3, 14, 2, 8, 10, 14, 25]
    count = numlist.count(14)
    print("Count is: ", count)

    numlist.reverse()
    print("Reversal of list", numlist)

    numlist.sort()

    print("Sorted list" , numlist)

    print()

    # how to use the sort() function with mixed-case lists
    foodlist = ["orange", "apple", "Pear", "banana"]
    foodlist.sort()
    print("Sorted foodlist", foodlist)

    # how to use the key argument to fix the sort order
    foodlist.sort(key=str.lower)
    print("Sorted by key foodlist", foodlist)

    print()

    # how to use the sorted() function with mixed-case lists
    # results of simple sort
    foodlist = ["orange", "apple", "Pear", "banana"]
    sorted_foodlist = sorted(foodlist)
    print(sorted_foodlist)

    # how to use the key argument to fix the sort order
    sorted_foodlist = sorted(foodlist, key=str.lower)
    print(sorted_foodlist)

    # Note that the sorted() function creates a new list, but the sort() does not

    # min() and max()
    numlist = [5, 6, 7, 8, 50, 90, 4, 10, 25]
    minimum = min(numlist)
    print("Min number", minimum)

    maximum = max(numlist)
    print("Max number", maximum)

    numlist = [70, 71, 72, 80, 65, 20]
    choice = random.choice(numlist)
    print("Choice: ", choice)

    random.shuffle(numlist)
    print("Random shuffle: ", numlist)

if __name__ == "__main__":
    main()
