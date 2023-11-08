#calculator using python programming
#user input from two numbers to calculate

#operations usage

while True:
    print("Choose an operation from the list:")
    print()
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Exit")

#operation input
    option = int(input("Enter an option or 0 to exit: "))
#performs an operatiopn based on an input from user
    if option == 0:
        break
    if option in(1, 2, 3, 4):
        # Prompt for user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if option == 1:
            print("The sum is:", num1 + num2)
        elif option == 2:
            print("The difference is:", num1 - num2)
        elif option == 3:
            print("The product is:", num1 * num2)
        elif option == 4:
            if num2 != 0:
                print("The quotient is:", num1 / num2 )
            else:
                print("cannot divide by zero")
    else:
        print("Invalid input")
            
            

        
    


