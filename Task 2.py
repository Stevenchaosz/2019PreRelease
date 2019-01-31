# The app intends to display interactive auction board information including
# Item number, number of bids, description and reserve price.

# Task 1
product_selling = 0  # Initialization
while True:
    product_selling = int(input("How many items are you going to sell"))
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
    _name = str(input("Please enter the item name: "))
    _description = str(input("Please enter the item description: "))
    _price = float(input("Please enter the reserve price: "))

    name_list.append(_name)
    description_list.append(_description)
    reserve_price_list.append(_price)

# Task 2

highest_bid_list = [0] * product_selling
buyer_number_list = ["1", "2", "3", "4", "5", "6"]
item_highest_bid_holder_list = [""]*10  # used in task 3

while True:
    # Print all item and item number
    for i in range(len(name_list)):
        _item_num = str(item_number_list[i])
        current_item_name = str(name_list[i])
        print(_item_num + ": " + current_item_name)

    restart = False
    exit_loop = False
    name_search = input("Please enter the item name: ")
    name_search = name_search.casefold()
    if name_search not in name_list:
        print("Item number invalid, enter again.")
        continue
    else:
        search_index = name_list.index(name_search)
        current_description = description_list[search_index]
        item_highest_bid = float(highest_bid_list[search_index])
        item_highest_bid_with_dollar_sign = "$" + str(item_highest_bid)
        print("Details: " + current_description)
        print("Current highest bit is " + item_highest_bid_with_dollar_sign)

        purchase_status = input("\nDo you want to purchase? Y/N: ")
        purchase_status = purchase_status.casefold()

        while purchase_status == "y":
            buyer_number_check = str(input("Please enter your buyer number: "))
            while buyer_number_check in buyer_number_list:
                print("\nIdentity verified.")
                buyer_bid = float(input("Please enter your bid: "))
                # no type check or type conversion is need because if it is not a number,
                # then it will automatically fail the condition
                if buyer_bid > item_highest_bid:
                    item_highest_bid = buyer_bid
                    highest_bid_list[search_index] = float(item_highest_bid)
                    bid_number_list[search_index] += 1
                    item_highest_bid_holder_list[search_index] = buyer_number_check
                    print("Congratulation! Your bid is the current highest.")
                    print("\nYet you are free to give another higher bid.")
                    while True:
                        further_bid = input("Do you want to give another bid or allow others to bid? Y/N")
                        further_bid = further_bid.casefold()
                        if further_bid == "y":
                            restart = True
                            break
                        elif further_bid == "n":
                            exit_loop = True
                            break
                        else:
                            print("Sorry, error in input")
                            continue
                else:
                    print("Your bid is lower than the current highest bid, please try again.\n")
                    continue
                if restart:
                    break
                elif exit_loop:
                    break
            else:
                print("Identify verification failed. Please try again.")
                continue
            if restart:
                break
            elif exit_loop:
                break
        else:
            print("Purchasing process canceled.\n")
            continue
        if restart:
            print()
            continue
        elif exit_loop:
            break
