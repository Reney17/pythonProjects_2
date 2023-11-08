import sys
from ctuClass import ctuStock
from os import system

from ctuClass import  *

#--Instantiation ctuClass objects------#

shop1 = ctuStock("Default","Default",0,0,0)
shop2 = ctuStock("Default","Default",0,0,0)
shop3 = ctuStock("Default","Default",0,0,0)
shop4 = ctuStock("Default","Default",0,0,0)

userInput = 0
heading = ''
stock = []
items = []
itemPrices = []
itemQuantity = []


#---------------------------------Functions--------------------------------#
def addStock(item,price,quantity):
    items.append(f"Item:{item}")
    itemPrices.append(f"Price:Rs{price}")
    itemQuantity.append(f"Quantity:{quantity}")


def showMenu():
    print('Welcome to CTU Technologies \n 1.Shop Management \n 2.Sales \n 3.Returns \n 4.Stock \n 99.Exit')

def shopManagementMenu():
    print('Shop Management \n 1.Change Shop Name \n 2.Change shop location \n 3.Display current shops \n'
          ' 4.Display all shops information \n 0.back')

def showShops():
    print(f"Change shop name \n \n select a shop \n 1. {shop1.shopName} \n "
          f"2. {shop2.shopName} \n 3. {shop3.shopName} \n 4. {shop4.shopName} \n 0.Back")

def showShopLocations():
    print(f"Change shop location \n \n select a shop \n 1.{shop1.shopName} ,{shop1.shopLocation} \n "
          f"2.{shop2.shopName} ,{shop2.shopLocation} \n 3.{shop3.shopName},{shop3.shopLocation} \n"
          f" 4.{shop4.shopLocation},{shop4.shopLocation} \n 0.Back")
def currentShops():
    print(f"Change shop location \n \n select a shop \n 1.{shop1.shopName} ,{shop1.shopLocation} \n "
          f"2.{shop2.shopName} ,{shop2.shopLocation} \n 3.{shop3.shopName},{shop3.shopLocation} \n"
          f" 4.{shop4.shopLocation},{shop4.shopLocation} \n 0.Back")
def stockMenu():
    print("1.Display Stock")
    print("2.Add Stock")
    print("0.Back")
def displayStock():
    for item in stock:
        print(item)

def displayShopsInfo():
    print('\n---------------\n Shop Name: '+shop1.shopName +'\n Shop Location :'+shop1.shopLocation +
          ' \n Number of Custommers : '+ str(shop1.customers) + '\n Current Sales :' +
           str(shop1.sales) + '\n Returns : ' + str(shop1.returns) +'\n---------------')
    print('\n---------------\n Shop Name: '+shop2.shopName +'\n Shop Location :'+shop2.shopLocation +
          ' \n Number of Custommers : '+ str(shop2.customers) + '\n Current Sales :' +
           str(shop2.sales) + '\n Returns : ' + str(shop2.returns) +'\n---------------')
    print('\n---------------\n Shop Name: '+shop3.shopName +'\n Shop Location :'+shop3.shopLocation +
          ' \n Number of Custommers : '+ str(shop3.customers) + '\n Current Sales :' +
           str(shop3.sales) + '\n Returns : ' + str(shop3.returns) +'\n---------------')
    print('\n---------------\n Shop Name: '+shop4.shopName +'\n Shop Location :'+shop4.shopLocation +
          ' \n Number of Custommers : '+ str(shop4.customers) + '\n Current Sales :' +
           str(shop4.sales) + '\n Returns : ' + str(shop4.returns) +'\n---------------')

def changeShopName(userInput):
    if userInput == 1:
        shop1.shopName = input("Type the new shop name: ")
        return showShops()
    elif userInput == 2:
        shop2.shopName = input("Type the new shop name: ")
        return showShops()
    elif userInput == 3:
        shop3.shopName = input("Type the new shop name: ")
        return showShops()
    elif userInput == 4:
        shop4.shopName = input("Type the new shop name: ")
        return showShops()

def changeShopLocation(userInput):
    if userInput == 1:
        shop1.shopLocation = input("Enter a location Free State,Gauteng,KZN,Limpopo: ")
        return showShopLocations()
    elif userInput == 2:
        shop2.shopLocation = input("Enter a location Free State,Gauteng,KZN,Limpopo: ")
        return showShopLocations()()
    elif userInput == 3:
        shop3.shopLocation = input("Enter a location Free State,Gauteng,KZN,Limpopo: ")
        return showShopLocations()()
    elif userInput == 4:
        shop4.shopLocation = input("Enter a location Free State,Gauteng,KZN,Limpopo: ")
        return showShopLocations()()



def switch(userInput):
    if userInput == 1:
        return shopManagementMenu()

    elif userInput == 2:
        return shopManagementMenu()

    elif userInput == 3:
        return shopManagementMenu()

    elif userInput == 4:
        return shopManagementMenu()

    elif userInput == 99:
        return sys.exit()






#--------------------------------main program loop--------------------------------#

while userInput != 99:
    if userInput == 0:
        heading = 'Home'
        showMenu()
    #---------------Option 1 Shop Management---------------#

    userInput = int(input("select an option or 99 to exit: "))
    if userInput == 1 and heading == 'Home':
        shopManagementMenu()
        heading = "ShopManagement"
        userInput = int(input("select an option or 99 to exit: "))

        if userInput == 1 and heading == "ShopManagement":
            showShops()
            heading = "ChangeShopName"
            while heading == "ChangeShopName":
                userInput = int(input("select an option or 99 to exit: "))
                changeShopName(userInput)
                if userInput == 0:
                    heading = 'Home'
                    showMenu()
        if userInput == 2 and heading == "ShopManagement":
            showShopLocations()
            heading = "ChangeShopLocation"
            while heading == "ChangeShopLocation":
                userInput = int(input("select an option or 99 to exit: "))
                changeShopLocation(userInput)
                if userInput == 0:
                    heading = 'Home'
                    showMenu()
        if userInput == 3 and heading == "ShopManagement":
            currentShops()
        if userInput == 4 and heading == "ShopManagement":
            displayShopsInfo()

    # ---------------Option 2 Sales---------------#

    if userInput == 2 and heading == "Home":
       ## shopManagementMenu()
        heading = "Sales"
        iCount = 0
        for sale in items:
            iCount+=1
            print(f"{iCount}.{sale}")
        selectedItem = int(input("Select item to buy:"))
        numOfItems = int(input("Enter number of items:"))
        showShops()
        userInput = int(input("Select shop:"))



    # ---------------Option 3 Returns---------------#

    if userInput == 3 and heading == "Home":
        ##shopManagementMenu()
        heading = "Returns"
        system('cls')

    # ---------------Option 4 Stock---------------#

    if userInput == 4 and heading == "Home":
        stockMenu()
        heading = "Stock"
        userInput = int(input("select an option or 99 to exit: "))
    if userInput == 1 and heading == "Stock":
        displayStock()
        print("0.Back")
    if userInput == 2 and heading == "Stock":
        try:
            itemName = input("Enter item name :")
            itemPrice = float(input("Enter item price :"))
            item_Quantity = float(input("Enter item quantity :"))
            if len(itemName) > 0 and itemPrice >= 1 and item_Quantity >= 1:
                addStock(itemName, itemPrice, item_Quantity)
                stock.append(f"Item name :{itemName} - Price:{itemPrice} - Quantity in stock:{item_Quantity}")
                print("Item added successfuly")
            else:print("invalid data entered")
        except:
            print("Check price or quantity value")
        finally:
            stockMenu()