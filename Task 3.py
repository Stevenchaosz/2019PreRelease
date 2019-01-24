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
    print()
    print()
    name_search = input("Please enter the item name: ")
    name_search = name_search.casefold()
    if name_search not in item_name_list:
        print("Item number invalid, enter again.")
        continue
    else:
        search_index = item_name_list.index(name_search)
        current_description = description_list[search_index]
        item_highest_bid = int(highest_bid_price_list[search_index])
        item_highest_bid_with_dollar_sign = "$" + str(item_highest_bid)
        print("Details: " + current_description)
        print("Current highest bit is " + item_highest_bid_with_dollar_sign)

        purchase_status = input("\nDo you want to purchase? Y/N: ")
        purchase_status = purchase_status.casefold()

        while purchase_status == "y":
            buyer_number_check = str(input("\nPlease enter your buyer number: "))
            while buyer_number_check in buyer_number_list:
                print("Identity verified.")
                buyer_bid = int(input("\nPlease enter your bid: "))
                # no type check or type conversion is need because if it is not a number,
                # then it will automatically fail the condition
                if buyer_bid > item_highest_bid:
                    item_highest_bid = buyer_bid
                    highest_bid_price_list[search_index] = int(item_highest_bid)
                    bid_number_list[search_index] += 1
                    item_highest_bid_holder_list[search_index] = buyer_number_check
                    print("Congratulation! Your bid is the current highest.")
                    print("Yet you are free to give another higher bid.")
                    while True:
                        further_bid = input("\nDo you want to give another bid or allow others to bid? Y/N")
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
under_reserve_price_item_number_list = []
no_bid_item_number_list = []
sold_status_list = ["no"] * 10
total_fee_list = []
total_price = 0
print()
print()

for x in range(len(highest_bid_price_list)):
    index_number = int(x)
    if int(highest_bid_price_list[x]) == 0:
        no_bid_item_number_list.append(index_number + 1)
        sold_status_list[x] = "no"
    elif int(highest_bid_price_list[x]) < int(reserve_price_list[x]) and int(highest_bid_price_list[x]) != 0:
        under_reserve_price_item_number_list.append(index_number + 1)
        sold_status_list[x] = "no"
    elif int(highest_bid_price_list[x]) > int(reserve_price_list[x]):
        highest_price_item_number_list.append(index_number+1)
        sold_status_list[x] = "yes"
        total_price = total_price + int(highest_bid_price_list[x]*1.1)
    
#    fee = [0]*len(highest_price_item_number_list)
#    total_fee_list.append((1 + 0.1) * int(highest_bid_price_list[x]))
#    total_fee_string = str(int(total_fee_list[x]))
#    highest_item_number = str(x + 1)
#    print("The total price of " + highest_item_number + " is $"+total_fee_string)

print("\n\nTotal price is $"+str(total_price))

if len(under_reserve_price_item_number_list) != 0:
    print("\n")
    
for y in range(len(under_reserve_price_item_number_list)):
    under_reserve_price_index = under_reserve_price_item_number_list[y]
    under_reserve_price_index_string = str(under_reserve_price_index)
    underbid_price = highest_bid_price_list[under_reserve_price_index-1]
    underbid_price_string = str(underbid_price)
    print("Item Number "+under_reserve_price_index_string+" has a highest price of $"+underbid_price_string+". But the price is lower than the reserve price.")

if len(no_bid_item_number_list) != 0:
    print("\n")

for z in range(len(no_bid_item_number_list)):
    no_bid_item_number_index = no_bid_item_number_list[z]
    no_bid_item_number_index_string = str(no_bid_item_number_index)
    print("Item Number "+no_bid_item_number_index_string+" has no bid at all")

sold_item_quantity = str(len(highest_price_item_number_list))
under_reserve_price_item_quantity = str(len(under_reserve_price_item_number_list))
no_bid_quantity = str(len(no_bid_item_number_list))

print()
print(sold_item_quantity+" is/are sold.")
print(under_reserve_price_item_quantity+" is/are lower than reserve price.")
print(no_bid_quantity+ " has/have no bids.")
