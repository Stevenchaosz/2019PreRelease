# The app intends to display interactive auction board information including
# Item number, number of bids, description and reserve price.

NumberOfBid = []
Description = []
ReservePrice = []
ProductSelling = 0
ItemNo = []

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
CurrentDescription = str(input("Please enter the item description: "))
Description.append(CurrentDescription)
CurrentReservePrice = float(input("Please enter the price: "))
ReservePrice.append(CurrentReservePrice)
NumberOfBid.append(0)
print("\n")
print(ItemNo)
print(Description)
print(ReservePrice)
