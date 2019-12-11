###########################################
#
# listexamples2
#
# working with list
#
# copy, slice and concatenate lists
#
# copy module imported for deepcopy()
###########################################

import copy


def main():

    # make a shallow copy of a list
    # anything you do to one is reflected in both
    list_one = [1, 2, 3, 4, 5]
    list_two = list_one
    list_two[4] = 7
    print(list_one)
    print(list_two)

    print()

    # make a deep copy of a list
    # anything you do to one does NOT effect the other
    list_one = [1, 2, 3, 4, 5]
    list_two = copy.deepcopy(list_one)
    list_two[1] = 4
    print(list_one)
    print(list_two)

    print()

    # slicing lists
    # slice start and end arguments
    numbers = [52, 54, 56, 58, 60, 62]
    print(numbers)
    print(numbers[0:2])
    print(numbers[:2])
    print(numbers[4:])

    print()


    # concatenate
    inventory = ["staff", "robe"]
    chest = ["scroll", "pestle"]
    combined = inventory + chest
    print(inventory)
    inventory += chest
    print(inventory)
    print()
    print(combined)
    print()






if __name__ == "__main__":
    main()

