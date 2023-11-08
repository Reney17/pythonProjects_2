#   the following code is called mainmenu due to it's purpose of giving the user prompts to choose options,this is a CTU tech Menu written in python
#   Importing from ctuClass
import sys
from ctuClass import ctuStock
from os import system

#   Four shop objects with default values(instantiating)
#   An object is an instance of a class
shop1 = ctuStock("Default","Default",0,0,0)
shop2 = ctuStock("Default","Default",0,0,0)
shop3 = ctuStock("Default","Default",0,0,0)
shop4 = ctuStock("Default","Default",0,0,0)

#   initializing user input

user_input = 0

#user_input = input("Select an option or 99 to exit:  ")

#----------FUNCTIONS FOR THE MENUS--------#
#   Function to display the main menu
def display_main_menu():
    print("Welcome to CTU Technologies")
    print()
    print("1. Shop Management")
    print("2. Sales")
    print("3. Returns")
    print("4. Stock")
    print("99. Exit")
    # return display_main_menu()

#   Function to display the shop management menu
def display_shop_management_menu():
    print("Shop Management Menu:")
    print("1. Change shop Name")
    print("2. Change shop Location")
    print("3. Display all current shops")
    print("4. Display all shops Information")
    print("0. Back")
    # return display_shop_management_menu()

#   Function to display Change shop Name
def change_shop_name():
    print("Change Shop name")
    print()
    print("Select Shop")
    print(f"1. {shop1.shopName}")
    print(f"2. {shop2.shopName}")
    print(f"3. {shop3.shopName}")
    print(f"4. {shop4.shopName}")
    print("0. Exit")
    # return change_shop_name()

#   Function to display Change shop Location
def change_shop_location():
    print("Change Shop Location")
    print()
    print("Select Shop")
    print(f"1. {shop1.shopLocation}, {shop1.shopName}")
    print(f"2. {shop2.shopLocation}, {shop2.shopName}")
    print(f"3. {shop3.shopLocation}, {shop3.shopName}")
    print(f"4. {shop4.shopLocation}, {shop4.shopName}")
    print("0. Back")
    # return change_shop_location()

#   Function to display current shops
def current_shop():
    print("Current Shops")
    print()
    print(f"1. {shop1.shopLocation}, {shop1.shopName}")
    print(f"2. {shop2.shopLocation}, {shop2.shopName}")
    print(f"3. {shop3.shopLocation}, {shop3.shopName}")
    print(f"4. {shop4.shopLocation}, {shop4.shopName}") 
    print("0. Back")  
     
#   write a function to change shop name
def change_shops(user_input):
    if user_input == 1:
        shop1.shopName = input("Type the new shop name  ")
        return change_shop_name()
    elif user_input == 2:
        shop2.shopName = input("Type the new shop name: ")
        return change_shop_name()
    elif user_input == 3:
        shop3.shopName = input("Type the new shop name: ")
        return change_shop_name()
    elif user_input == 4:
        shop4.shopName = input("Type the new shop name: ")
        return change_shop_name()
    elif user_input == 99:
        sys.exit()
    
#   write a function to change shop location
def change_locations(user_input):
    if user_input == 1:
        shop1.shopLocation = input("Enter a location Free State,Gauteng,KZN,Limpopo: ")
        return change_shop_location()
    elif user_input == 2:
        shop2.shopLocation = input("Enter a location Free State,Gauteng,KZN,Limpopo: ")
        return change_shop_location()
    elif user_input == 3:
        shop3.shopLocation = input("Enter a location Free State,Gauteng,KZN,Limpopo: ")
        return change_shop_location()
    elif user_input == 4:
        shop4.shopLocation = input("Enter a location Free State,Gauteng,KZN,Limpopo: ")
        return change_shop_location()
    
#   using the while loop to show the main menu

while user_input != 99:
    if user_input == 0:
        display_main_menu()
#   Option 1 Shop Management

    user_input = int(input("Select an option or 99 to exit: "))
    if user_input == 1:
        display_shop_management_menu()
        user_input = int(input("Select an option or 99 to exit: ")) #user input to check shop management option
        
        if user_input == 1:
            change_shop_name()
            user_input = int(input("Select an option or 99 to exit: "))
            
            while True:
                user_input = int(input("Select an option or 99 to exit: ")) #the while loop to run the functiion to change shop name
                change_shops(user_input)
                if user_input == 0:
                    display_main_menu()
            
        if user_input == 2:
            change_shop_location()
            user_input = int(input("Select an option or 99 to exit: "))
            
        while True:
            user_input = int(input("Select an option or 99 to exit: ")) #the while loop to run the functiion to change shop location
            change_locations(user_input)
            if user_input == 0:
                display_main_menu()
                
            if user_input == 3:
                current_shop()
                
            if user_input == 4:
                current_shop()

#--------------End of the code--------written and edited by a CTU programming foundation student

        
        