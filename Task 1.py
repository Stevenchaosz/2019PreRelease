# The app intends to display interactive auction board information including
# Item number, number of bids, description and reserve price.

ItemName = ["Phone", "Postcard", "Car", "Pen", "Tablet", "Pencil Case", "Laptop", "Mouse", "Keyboard", "收藏加购物车十元返现"]
NumberOfBid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Description = ["iPhone XS", "New Zealand City View", "BMW i8", "Schneider Limited Edition", "iPad Pro 12.9in", "Kokuyo Limited", "ASUS Zenbook Pro 15", "Magic Mouse", "Cherry MX. 8.0", "勿拍此项"]
ReservePrice = [300, 15, 50000, 100, 2027, 50, 1099, 129, 699]
ProductSelling = 0
ItemNo = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# while True:
#         ProductSelling = int(input("Number of selling items: "))
#         if ProductSelling < 10:
#             continue
#             print("Please enter an item number bigger than 10.")
#         else:
#             break
#
# for i in range(ProductSelling):
#     CurrentItemNo = int(input("Assign an item number: "))
#     if CurrentItemNo not in ItemNo:
#         ItemNo.append(CurrentItemNo)
#     else:
#         print("Item number is not unique, please try again.")
#         continue
#         CurrentDescription = str(input("Please enter the item description: "))
#         Description.append(CurrentDescription)
#         CurrentReservePrice = float(input("Please enter the price: "))
#         ReservePrice.append(CurrentReservePrice)
#         NumberOfBid.append(0)
print("\n")
print(ItemNo)
print(ItemName)
print(Description)
print(ReservePrice)
