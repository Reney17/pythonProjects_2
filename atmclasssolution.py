# python program 

pin = 1234
balance = 1000
attempts = 3
restart = 'y'

print("****Welcome to CTU ATM****")

while attempts > 0:
    code=int(input("Please enter a pin: "))
    if code == pin:
        while restart not in ("no", "No" , "n", "N"):
            print("**select from the following option**")
            print()
            print("1. Balance")
            print("2. Withdrawal")
            print("3. Deposit")    
            print("4. Print statement")
            print("5. Return Card")
            option =int(input("select an option above: "))
            if option == 1:
                print("Your current Balance is: ", balance)
                restart=input("would you like to go back(y/n)")
                if restart in ("no", "No", "n", "N"):
                    break
            elif option ==2:
                withdraw = int(input("Please enter the amount you want to withdraw: "))
                balance = balance - withdraw
                print("you have withdrawn", withdraw,"your new balance is", balance)
                restart=input("would you like to go back(y/n)")
                if restart in ("no", "No", "n", "N"):
                    break
            elif option == 3:
                deposit = int(input("The amount you want to deposit: "))
                balance = balance + deposit
                print("you have depositted", deposit, "your new balance is", balance)
                restart=input("would you like to go back(y/n)")
                if restart in ("no", "No", "n", "N"):
                    break
            elif option == 4:
                print("your current balance is:", balance)
                print()
            elif option == 5:
                print("Please wait while your card is returned..")
                print()
                print("Thank you for your service")
                break
            else:
                print("you have entered an invalid option")
                restart = ('y')
    elif code != pin:
        print("Incorrect pin")
        attempts = attempts - 1
        if attempts == 0:
            print("No more tries ")
            break