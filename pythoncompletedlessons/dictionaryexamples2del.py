###########################################
#
# dictionaryexamples2del
#  deleting
#
#
###########################################



def main():

    countries = {"CA": "Canada",
                 "US": "United States",
                 "GB": "Great Britain",
                 "MX": "Mexico"}

    print()
    print(countries)
    print()

    # code that checks if a key is in a dictionary before getting its value
    code = "US"
    if code in countries:
        country = countries[code]
        del countries[code]
        print(country + " was deleted.")
    else:
        print("There is no country for this code: " + code)

    print()
    print(countries)
    print()


    # using pop to delete
    print("pop example")
    print()
    country = countries.pop("MX")

    print()
    print(countries)
    print()



if __name__ == "__main__":
    main()
