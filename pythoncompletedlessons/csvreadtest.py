

###########################################
#
# csvreadstest
#
#
#
###########################################

import csv

FILENAME = "testthiscsv.txt"

def main():



    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0] + " (" + str(row[1]) + ")")



if __name__ == "__main__":
    main()

