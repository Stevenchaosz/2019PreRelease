# The app intends to display interactive auction board information including
# Item number, number of bids, description and reserve price.

# Task 1
product_selling = 0  # Initialization
print("Welcome to auction software.")

while True:  # Prompt for number of selling item & check if it is greater than 10
    product_selling = int(input("How many items are you going to sell: "))
    if product_selling < 10:
        print("Error, please enter more than 10 products.")
    else:
        break

name_list = []  # list storing item name
bid_number_list = [0]*product_selling  # list storing bid numbers for each item
description_list = []  # list storing item description
reserve_price_list = []  # list storing item reserved price
item_number_list = list(range(1, product_selling+1))

for i in range(product_selling):  # Prompt for item details
    _name = str(input("\nPlease enter the item name that you want to sell: "))
    _description = str(input("Please enter the item description: "))
    _price = float(input("Please enter the reserve price: "))

    name_list.append(_name)
    description_list.append(_description)
    reserve_price_list.append(_price)

print("\n")
print(name_list)
print(description_list)
print(reserve_price_list)
