###########################################
#
# dictionaryexamples
#  accessing
#
#
###########################################



def main():

    countries = {"CA": "Canada",
                 "US": "United States",
                 "GB": "Great Britain",
                 "MX": "Mexico"}

    # code that checks if a key is in a dictionary before getting its value
    code = "GB"
    if code in countries:
        country = countries[code]
        print(country)
    else:
        print("There is no country for this code: " + code)

    # use get method as an alternative to the above
    print()
    print("Using get method")
    print()
    country = countries.get("AA")
    print(country)  # will return None if not in dictionary






if __name__ == "__main__":
    main()
