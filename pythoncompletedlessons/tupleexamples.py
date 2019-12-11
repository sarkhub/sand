###########################################
#
# tupleexamples
#
# working with tuples
#
###########################################



def get_location():
    # compute values of x, y, z
    x = 10
    y = 20
    z = x + y
    return x, y, z


def main():

    stats = (48.0, 30.5, 20.2, 100.0, 48.0)

    print(stats)

    # access items in the tuple
    print(stats[-1])                 # last item
    print(stats[1:2])                # (30.5,)
    print(stats[1:3])                # (30.5, 20.2)
    print(stats[1:4])                # (30.5, 20.2, 100.0)


    print()

    # call get_location and unpack the returned tuple
    x, y, z = get_location()
    print("x: ", x)
    print("y: ", y)
    print("z: ", z)


if __name__ == "__main__":
    main()

