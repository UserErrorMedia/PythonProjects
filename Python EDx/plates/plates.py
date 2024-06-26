#This code is a proof of concept for validating correct structure of a license plate. Main use could be for validating usernames or passwords on a login page of an app

def main():
    plate = input("Plate: ")
    if not plate.isalnum() or (len(plate) < 2 or len(plate) > 6):
        print("Invalid")
        return False

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if   s.isalpha() or s[:2].isalpha() and s[-2:].isnumeric() and s[-2:][0] != "0":
        return True
    else:
        return False
main()