#This script eliminates all vowels in words or groups of words

tweet = input("Input: ")
tweet = tweet.strip()
print (tweet, end="")

list = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

for c in tweet:
    if not c in list:
        print(c, end="")

print()