# The app intends to display interactive auction board information including
# Item number, number of bids, description and reserve price.

# Task 1

item_name_list = ["phone", "postcard", "car", "pen", "tablet", "pencil case", "laptop", "mouse", "keyboard", "收藏加购物车十元返现"]
bid_number_list = [0]*10
description_list = ["iPhone XS", "New Zealand City View", "BMW i8", "Schneider Limited Edition", "iPad Pro 12.9in", "Kokuyo Limited", "ASUS Zenbook Pro 15", "Magic Mouse", "Cherry MX. 8.0", "勿拍此项"]
reserve_price_list = [300, 15, 50000, 100, 2027, 50, 1099, 129, 699, 1000000000]
item_number_list = list(range(1, 11))

# Task 2

highest_bid_price_list = [0] * 10
buyer_number_list = ["1", "2", "3", "4", "5", "6"]
item_highest_bid_holder_list = [""]*10  # used in task 3


search_index = 0
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

# Task 3
highest_price_item_number_list = []
under_reserved_price_item_number_list = []
no_bid_item_number_list = []
sold_status = ["no"]*10

for x in range(len(reserve_price_list)):
    index_number = int(x)
    if float(highest_bid_price_list[x]) < float(reserve_price_list[x]):
        under_reserved_price_item_number_list.append(index_number+1)
        sold_status[x] = "no"
    elif float(highest_bid_price_list[x]) > float(reserve_price_list[x]):
        highest_price_item_number_list.append(index_number+1)
        sold_status[x] = "yes"
    elif float(highest_bid_price_list[x]) == 0:
        no_bid_item_number_list.append(index_number+1)
        sold_status[x] = "no"

    fee = [0]*len(highest_price_item_number_list)
    total_fee = [0]*len(highest_price_item_number_list)
    total_fee[x] = (1+0.1)*float(highest_bid_price_list[x])
    total_fee_string = str(total_fee)
    highest_item_number = str(x+1)
    print("The total fee of "+highest_item_number+"is "+total_fee_string)


