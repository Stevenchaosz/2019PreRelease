# The app intends to display interactive auction board information including
# Item number, number of bids, description and reserve price.

# Task 1
# Allow auction company to enter item details.
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

# Task 2
# Allow buyers to purchase
highest_bid_list = [0] * product_selling  # list storing highest bid for each item
buyer_number_list = ["1", "2", "3", "4", "5", "6"]  # buyer number list
item_highest_bid_holder_list = [""]*10  # used in task 3
buyer_number_check = "0"  # initialize buyer number; prevent void input
cookie = False  # initialize cookie; avoid double identification on the same buyer
while True:
    purchase_status = "no"
    print("\nWelcome to auction! ")

    for i in range(len(name_list)):  # Print all item and their item numbers
        _item_num = str(item_number_list[i])
        current_item_name = str(name_list[i])
        print(_item_num + ": " + current_item_name)

    if buyer_number_check == "0":  # Prompt for buyer number
        print("If you want to bid, \n"
              "please enter your buyer number ")
        buyer_number_check = str(input("To terminate the transaction, "
                                       "please enter 'exit': "))
    buyer_number_check = buyer_number_check.casefold()  # accept uppercase and lowercase

    while buyer_number_check in buyer_number_list:  # bidding procedure
        if not cookie:  # avoid double identification on the same buyer
            print("\nIdentity verified.")
        item_to_buy = input("\nPlease enter the item name that you want to bid: ")
        item_to_buy = item_to_buy.casefold()
        if item_to_buy not in name_list:  # check if buyer number in list
            print("Item number invalid, try again.")
            continue

        search_index = name_list.index(item_to_buy)  # search for item
        current_description = description_list[search_index]  # find description
        item_highest_bid = float(highest_bid_list[search_index])
        item_highest_bid_with_dollar_sign = "$" + str(item_highest_bid)
        print("Details: " + current_description)
        print("Current highest bit is " + item_highest_bid_with_dollar_sign)

        while True:  # Prompt for higher bid
            buyer_bid = float(input("Please enter your bid: "))
            if buyer_bid > item_highest_bid:  # check if bid is higher than current highest
                item_highest_bid = buyer_bid
                highest_bid_list[search_index] = float(item_highest_bid)
                bid_number_list[search_index] += 1
                item_highest_bid_holder_list[search_index] = buyer_number_check
                print("Congratulation! Your bid is the current highest bid.")
                cookie = True
                break
            else:
                print("Sorry, bid lower than current highest bid. Try again.")

        while True:  # prompt for another bid
            purchase_status = str(input("Do you want to bid for another item? Y/N"))
            purchase_status = purchase_status.casefold()
            if purchase_status != "y" or purchase_status != "n":
                print("Error, please try again.")
            break
        break
    if purchase_status == "n":
        buyer_number_check = "0"
    if buyer_number_check == "exit":
        break
    if buyer_number_check not in buyer_number_list:
        print("Buyer number invalid, try again. ")
        buyer_number_check = "0"