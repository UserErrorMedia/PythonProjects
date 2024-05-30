# Prompt user for greeting
greeting = input("Someone walks in the door, you say... ")
greeting = greeting.lower().strip()

# "Hello" = $0
# Starts with "H" but not "Hello" = $20
# All others = $100

if greeting == "hello" or greeting.startswith("hello"):
    print("$0")
elif greeting != "hello" and greeting.startswith("h"):
    print("$20")
else:
    print("$100")