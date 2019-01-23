# The app intends to display interactive auction board information including
# Item number, number of bids, description and reserve price.

# Task 1

ItemName = ["phone", "postcard", "car", "pen", "tablet", "pencil case", "laptop", "mouse", "keyboard", "收藏加购物车十元返现"]
NumberOfBid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Description = ["iPhone XS", "New Zealand City View", "BMW i8", "Schneider Limited Edition", "iPad Pro 12.9in", "Kokuyo Limited", "ASUS Zenbook Pro 15", "Magic Mouse", "Cherry MX. 8.0", "勿拍此项"]
ReservePrice = [300, 15, 50000, 100, 2027, 50, 1099, 129, 699, 1000000000]
ProductSelling = 0
ItemNo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# Task 2

for i in range(len(ItemName)):
    ItemNoCurrent = str(ItemNo[i])
    ItemNameCurrent = str(ItemName[i])
    print(ItemNoCurrent+": "+ItemNameCurrent)

while True:
    SearchDescription = input("Please enter the item name: ")
    SearchDescription = SearchDescription.casefold()
    if SearchDescription not in ItemName:
        print("Item number invalid, enter again.")
        continue
    else:
        CurrentPosition = ItemName.index(SearchDescription)
        CurrentDescription = Description[CurrentPosition]
        print("Details: "+CurrentDescription)
        print("Current highest bit is "+)