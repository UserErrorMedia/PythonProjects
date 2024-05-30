#This script is a simulation of a product in a vending machine where the item total cost is 50 cents. The code only accepts quarters, dimes and nickels and runs down until the amount is fulfilled

amount_due = 50
list = [25, 10, 5]
change_owed = abs(amount_due)

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coins = int(input("Insert Coin: "))
    if coins in list:
        amount_due -= coins;

print(f"Change Owed: {abs(change_owed)}")