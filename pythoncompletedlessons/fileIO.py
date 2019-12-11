###########################################
#
# fileIO
#
# use files
#
###########################################


def main():
    outfile = open("test.txt", "w")
    outfile.write("NEW X Test")
    outfile.close()

    print("write complete")

    infile = open("test.txt", "r")
    print(infile.readline())

    print("read complete")


if __name__ == "__main__":
    main()
