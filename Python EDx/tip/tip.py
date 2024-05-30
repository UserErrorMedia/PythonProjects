#This is a simple tip calculator app script

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    # Remove the "$" if present and convert to a float
    d = d.replace("$", "")
    return float(d)

def percent_to_float(p):
    # TODO
    # Remove the "%" and convert to a float
    p = p.replace("%", "")
    return float(p) / 100


main()