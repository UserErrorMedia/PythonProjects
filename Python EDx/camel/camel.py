#This script will convert text written in camel case to snake_case

response = input("camelCase: ")

print("snake_case: ", end="")

for c in response:
    if c.isupper():
        print("_" + c.lower(), end="")
    else:
        print(c, end="")
print()