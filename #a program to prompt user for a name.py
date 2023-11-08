#a program to prompt user for a name.then using the while loop in a situation where there is no name it should display to the user 
# "you did not enter your name"  then asks the user to enter name again (the finally print their name)




name = input("Enter your name: ")


while name == "":
     print("You did not enter your name")
     name = input("Enter your name: ")
   
     break
print("hello", name)
# name = input("Enter your name: ")

