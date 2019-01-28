# The app intends to display interactive auction board information including
# Item number, number of bids, description and reserve price.

# ItemName = ["phone", "postcard", "car", "pen", "tablet", "pencil case", "laptop", "mouse", "keyboard", "收藏加购物车十元返现"]
# NumberOfBid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Description = ["iPhone XS", "New Zealand City View", "BMW i8", "Schneider Limited Edition",
# "iPad Pro 12.9in", "Kokuyo Limited", "ASUS Zenbook Pro 15", "Magic Mouse", "Cherry MX. 8.0", "勿拍此项"]
# ReservePrice = [300, 15, 50000, 100, 2027, 50, 1099, 129, 699, 1000000000]
# # ProductSelling = 0
# ItemNo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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
print("\n")
print(item_number_list)
print(item_name_list)
print(description_list)
print(reserve_price_list)