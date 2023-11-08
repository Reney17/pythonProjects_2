#Building a calculator with python
#A function to add
def Addition(x,y):
    return x+y

#A function to subtract
def Subtraction(x,y):
    return x-y

#A function to multiply
def Multiplication(x,y):
    return x*y 

#A function to divide
def Division(x,y):
    return x/y

#while loop with TRUE(validator)
#Display menu options to the user
while True:
    print("Select an option:  ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5.Exit")
#Get the user's choice
    userinput = int(input("Please select 1/2/3/4/5: "))
    if userinput == 1:
        num1 = int(input("enter 1 number"))
        num2 = int(input("enter 2 number"))
        print("num1" , "+" ,"num2", "=" , Addition(num1,num2))
    elif userinput == 2:
        num1 = int(input("enter 1 number"))
        num2 = int(input("enter 2 number"))
        print("num1" , "-" ,"num2", "=" , Subtraction(num1,num2))
    elif userinput == 3:
        num1 = int(input("enter 1 number"))
        num2 = int(input("enter 2 number"))
        print("num1" , "*" ,"num2", "=" , Multiplication(num1,num2))
    elif userinput == 4:
        num1 = int(input("enter 1 number"))
        num2 = int(input("enter 2 number"))
        print("num1" , "/" ,"num2", "=" , Division(num1,num2))
    

    
    