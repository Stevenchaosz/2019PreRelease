# The app intends to display interactive auction board information including
# Item number, number of bids, description and reserve price.

# Task 1


while True:
        product_selling = int(input("Number of selling items: "))
        if product_selling < 10:
            print("Please enter an item number bigger than 10.")
            continue
        else:
            break

item_name_list = []
bid_number_list = [0]*product_selling
description_list = []
reserve_price_list = []
item_number_list = list(range(1, product_selling+1))
product_selling = 0

for i in range(product_selling):
    input_name = str(input("Please enter the item name: "))
    item_name_list.append(input_name)
    input_description = str(input("Please enter the item description: "))
    description_list.append(input_description)
    input_price = float(input("Please enter the reserve price: "))
    reserve_price_list.append(input_price)

# Task 2

highest_bit_list = [0]*10
buyer_number_list = ["1", "2", "3", "4", "5", "6"]
item_highest_bid_holder_list = [""]*10  # used in task 3

# for i in range(len(item_name_list)):
#     item_number_current = str(item_number_list[i])
#     current_item_name = str(item_name_list[i])
#     print(item_number_current + ": " + current_item_name)

while True:
    # Print all item and item number
    for i in range(len(item_name_list)):
        item_number_current = str(item_number_list[i])
        current_item_name = str(item_name_list[i])
        print(item_number_current + ": " + current_item_name)

    restart = False
    exit_loop = False
    name_search = input("Please enter the item name: ")
    name_search = name_search.casefold()
    if name_search not in item_name_list:
        print("Item number invalid, enter again.")
        continue
    else:
        search_index = item_name_list.index(name_search)
        current_description = description_list[search_index]
        item_highest_bid = float(highest_bid_price_list[search_index])
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
                    highest_bid_price_list[search_index] = float(item_highest_bid)
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
