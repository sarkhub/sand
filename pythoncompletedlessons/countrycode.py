###########################################
#
# countrycode
#
# dictionary
#
###########################################

def display_menu():
    print("COMMAND MENU")
    print("view - view country name")
    print("add - add a country")
    print("del - delete a country")
    print("exit - exit program")
    print()


def display_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    line = "Country codes: "
    for code in codes:
        line += code + " "
    print(line)


def view(countries):
    display_codes(countries)
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print("Country name: " + name + ".\n")
    else:
        print("There is no country with that code.\n")


def add(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(name + " is already using this code.\n")
    else:
        name = input("Enter country code: ")
        name = name.title()
        countries[code] = name
        print(name + " was added.\n")


def delete(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print(name + " was deleted.\n")
    else:
        print("There is no country with that code.\n")


def main():
    countries = {"CA": "Canada",
                 "US": "Untited Stated",
                 "MX": "Mexico"}

    display_menu()
    while True:
        command = input("Command: ")
        command = command.lower()
        if command == "view":
            view(countries)
        elif command == "add":
            add(countries)
        elif command == "del":
            delete(countries)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")



if __name__ == "__main__":
    main()
