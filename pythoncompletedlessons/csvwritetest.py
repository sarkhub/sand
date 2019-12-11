

###########################################
#
# csvwritestest
#
#
#
###########################################

import csv

FILENAME = "testthiscsv.txt"

def main():

    movies = [["New Movie", 1990],
              ["X", 2001],
              ["Y", 2019]]

    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(movies)


if __name__ == "__main__":
    main()

