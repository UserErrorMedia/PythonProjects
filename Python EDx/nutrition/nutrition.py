#This script is a proof of concept for an app that tracks calories. The list provided is composed of common fruits as an example.

# Prompt user for a fruit
fruit = input("Item: ")
fruit = fruit.lower()

fruits = {
    "avocado" : 50,
    "apple" : 130,
    "banana" : 110,
    "cantaloupe" : 50,
    "grapefruit" : 60,
    "grapes" : 90,
    "honeydew melon" : 50,
    "kiwifruit" : 90,
    "lemon" : 15,
    "lime" : 20,
    "nectarine" : 60,
    "orange" : 80,
    "peach" : 60,
    "pineapple" : 50,
    "pear" : 100,
    "plums" : 70,
    "strawberries" : 50,
    "sweet cherries" : 100,
    "tangerine" : 50,
    "watermelon" : 80
}

if fruit in fruits:
    print("Calories: ", + fruits[fruit])