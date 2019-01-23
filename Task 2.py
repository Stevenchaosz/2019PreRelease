# The app intends to display interactive auction board information including
# Item number, number of bids, description and reserve price.

# Task 1

item_name_list = ["phone", "postcard", "car", "pen", "tablet", "pencil case", "laptop", "mouse", "keyboard", "收藏加购物车十元返现"]
bid_number_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
description_list = ["iPhone XS", "New Zealand City View", "BMW i8", "Schneider Limited Edition", "iPad Pro 12.9in", "Kokuyo Limited", "ASUS Zenbook Pro 15", "Magic Mouse", "Cherry MX. 8.0", "勿拍此项"]
reserve_price_list = [300, 15, 50000, 100, 2027, 50, 1099, 129, 699, 1000000000]
item_number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# Task 2

highest_bit_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
buyer_id_list = [30001, 30002, 30003, 30004, 30005, 30006]

for i in range(len(item_name_list)):
    item_number_current = str(item_number_list[i])
    current_item_name = str(item_name_list[i])
    print(item_number_current + ": " + current_item_name)

while True:
    name_search = input("Please enter the item name: ")
    name_search = name_search.casefold()
    if name_search not in item_name_list:
        print("Item number invalid, enter again.")
        continue
    else:
        search_index = item_name_list.index(name_search)
        current_description = description_list[search_index]
        print("Details: " + current_description)
        item_highest_bit = "$" + str(highest_bit_list[search_index])
        print("Current highest bit is " + item_highest_bit)
        purchase_status = input("Do you want to purchase? Y/N: ")
        purchase_status = purchase_status.casefold()
        if purchase_status == "y":
            buyer_id_check = input("Please enter your buyer ID")
        else:
            print("Purchasing process canceled.\n")
            continue
