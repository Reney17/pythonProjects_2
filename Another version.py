
print("Welcome to CTU Technologies")
print("1. Shop Management")
print("2. Sales")
print("3. Returns")
print("4. Stock")
print("99. Exit")

optionSelected = int(input("Select an option or 99 to exit: "))
print(type(optionSelected))

if optionSelected == 99:
    print("Goodbye, you have selected option 99")
    print("=============")
elif optionSelected == 1:
    print("Shop Management")
    print("1. Change shop name")
    print("2. Change shop location")
    print("3. Display current shops")
    print("4. Display all shop information")
    print("0. Back")
    shopManagementSelection = int(input("Select an option: "))
    
    if shopManagementSelection == 1:
        print("You have selected to change the shop name")
        print("Select a shop:")
        shop1 = "1. Default"
        print("2. Default")
        print("3. Default")
        print("4. Default")
        print("Back")
        shopChosen = int(input("Select an option: "))
        newShopName = input("Type the new shop name: ")

        print("Shop name was successfully changed to " + newShopName)

    elif shopManagementSelection == 2:
        print("You have selected to change the shop location")
    elif shopManagementSelection == 3:
        print("Display current shops")
    elif shopManagementSelection == 4:
        print("Display all shop information")
    elif shopManagementSelection == 0:
        print("You have selected to go back")
    else:
        print("Invalid selection")
elif optionSelected == 2:
    print("Sales options were selected")
elif optionSelected == 3:
    print("Returns options were selected")
elif optionSelected == 4:
    print("Stock options were selected")
else:
    print("Invalid selection")