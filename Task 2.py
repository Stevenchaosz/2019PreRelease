# The app intends to display interactive auction board information including
# Item number, number of bids, description and reserve price.

# Task 1
product_selling = 0  # Initialization
while True:
    product_selling = int(input("How many items are you going to sell: "))
    if product_selling < 10:
        print("Error, please enter more than 10 products.")
    else:
        break
name_list = []
bid_number_list = [0]*product_selling
description_list = []
reserve_price_list = []
item_number_list = list(range(1, product_selling+1))

for i in range(product_selling):
    _name = str(input("\nPlease enter the item name that you want to sell: "))
    _description = str(input("Please enter the item description: "))
    _price = float(input("Please enter the reserve price: "))

    name_list.append(_name)
    description_list.append(_description)
    reserve_price_list.append(_price)

# Task 2
highest_bid_list = [0] * product_selling
buyer_number_list = ["1", "2", "3", "4", "5", "6"]
item_highest_bid_holder_list = [""]*10  # used in task 3
buyer_number_check = "0"
loop_status = False
while True:
    # Print all item and their item numbers
    print("\nWelcome to auction! ")

    for i in range(len(name_list)):
        _item_num = str(item_number_list[i])
        current_item_name = str(name_list[i])
        print(_item_num + ": " + current_item_name)

    if buyer_number_check == "0":
        print("If you want to give a bid, \n"
              "please enter your buyer number ")
        buyer_number_check = str(input("To terminate the transaction, "
                                       "please enter 'exit': "))
    purchase_status = "no"
    buyer_number_check = buyer_number_check.casefold()
    if buyer_number_check == "exit":
        break
    while buyer_number_check in buyer_number_list:
        if not loop_status:
            print("\nIdentity verified.")
        name_search = input("\nPlease enter the item name that you want to give a bid: ")
        name_search = name_search.casefold()
        if name_search not in name_list:
            print("Item number invalid, try again.")
            continue
        search_index = name_list.index(name_search)
        current_description = description_list[search_index]
        item_highest_bid = float(highest_bid_list[search_index])
        item_highest_bid_with_dollar_sign = "$" + str(item_highest_bid)
        print("Details: " + current_description)
        print("Current highest bit is " + item_highest_bid_with_dollar_sign)
        buyer_bid = float(input("Please enter your bid: "))
        if buyer_bid > item_highest_bid:
            item_highest_bid = buyer_bid
            highest_bid_list[search_index] = float(item_highest_bid)
            bid_number_list[search_index] += 1
            item_highest_bid_holder_list[search_index] = buyer_number_check
            print("Congratulation! Your bid is the current highest bid.")
            loop_status = True
        while True:
            purchase_status = str(input("Do you want to give another bid? Y/N"))
            purchase_status = purchase_status.casefold()
            if purchase_status != "y" or purchase_status != "n":
                print("Error, please try again.")
            break
        break

    if purchase_status == "y":
        continue
    elif purchase_status == "n":
        buyer_number_check = "0"
    if buyer_number_check not in buyer_number_list:
        print("Buyer number invalid, try again. ")
        buyer_number_check = "0"
        buyer_number_check = "0"
