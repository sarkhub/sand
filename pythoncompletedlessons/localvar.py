######################################
#
# localval
#
# used to demonstrate variable
#
######################################

def calc_tax(amount, tax_rate):
   tax = amount * tax_rate
   return tax


def main():
   tax = calc_tax(80.0, .05)
   print("Tax: ", tax)


if __name__ == "__main__":
    main()
