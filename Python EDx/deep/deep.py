#This script is based on the book "Hitchhikers Guide to the Galaxy" and only accepts variations of the number 42 as the answer to the greatest question ever asked

# Prompt user for the answer to the Great Question of Life, the Universe and Everything
answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
# Convert answer to lower case to match item in list
answer = answer.lower().strip()

# Create list of possible answers
answers = ["42", "forty two", "forty-two"]

if answer in answers:
    print("Yes")
else:
    print("No")