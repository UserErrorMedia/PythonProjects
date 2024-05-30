#This is a proof of concept for aggregating food items in a restaurant POS machine or app. It accumulates total cost of an order from specific food items offered by the establishment.

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        item = input("Item: ").title()
        if item in menu:
            price = menu[item]
            total += price
            print(f"Total: ${total:.2f}")
        else:
            print()
    except EOFError:
        print()
        break