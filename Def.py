def shopMenu():
    print("Shop Management")
    print("1. Change shop name")
    print("2. Change shop location")
    print("3. Display current shops")
    print("4. Display all shops information")
    print("0. Back")
    Selection = int(input("Selection option : "))

    if Selection == 1:
        shopManagementSelection()
    else:
        print("you have Selected wrong option")


# shopMenu()


def shopManagementSelection():
    print("You have selected to change the shop name")
    print("Select shop")
    # shop1 = "1. Default"
    print("2. Default")
    print("3. Default")
    print("4. Default")
    print("0. Back")
    # shopChosen = int(input("Select an option : "))
    newShopName = input("Type the new shop name : ")
    if newShopName == 1:
        print("Shop name was successfully changed to " + newShopName)
    # print(shopMenu())


# print(shopManagementSelection())
