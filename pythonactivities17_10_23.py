# #working with strings, numbers & conditional statements(if,elif,else)

# #1 create a simple python to check if 4 is less or greater than 5.

# num = 5
# if 4 < num:
#     print(f"4 is less than {num}")
# elif 4 > num:
#     print(f"4 is greater than {num}")
# else:
#     print(f"4 is equal to {num}")
# print()   
# num1 = int(input("enter first number: "))
# num2= int(input("enter second number: "))
# if num1 < num2:
#     print(f"{num1} is less than {num2}")
# elif num1 > num2:
#     print(f"{num1} is greater than {num2}")
# else:
#     print(f"{num1} is equal to {num2}")
# print()
    
# #2 a program to check if number is even or odd

# num = int(input("Enter a number:  "))# user input
# mod =num%2
# if mod > 0:
#     print("this is an odd number")
# else:
#     print("this is an even number")
    
# print()    
# num=4
# if num % 2 == 0:
#     print(f"{num} is an even number")
# else:
#     print(f"{num} is an odd number")
# print()
# #3 a program to determine the larger of two numbers.hint assign values 5 and 7  to variables

# num1 = 5  #assigning values to 5 and 7
# num2 = 7
# if num1 > num2:
#     print(f"{num1} is larger than {num2}")
# elif num1 < num2:
#     print(f"{num1} is not larger than {num2}")
# else:
#     print(f"{num1} is equal to {num2}")
# print()
# #4 a program to check if a number is divisable by both 5 and 3
# num = int(input("Enter a number:  "))
# if num%3 == 0:
#     if num%5 == 0:
#         print("The number is both divisable by 3 and 5")
#     else:
#         print("The number is only divisable by 3 and not 5")
# else:
#     if num%5 == 0:
#         print("divisable by 5 not divisable by 3")
#     else:
#         print("not divisable by both 3 and 5")

# print()       
# testnum=15
# if testnum%5 == 0 and testnum%3 == 0:
#     print(f"{testnum} is divisable by both by 3 and 5")
# else:
#     print(f"{testnum} is not divisable by both 3 and 5" )
# print()   
# #5 a program to check No is positive,negative or zero

# num=int(input("enter a number"))
# if num > 0:
#     print("it is a positive")
# elif num < 0:
#     print("it is a negative")
# else:
#     print("it is a zero")


# a program to find the maximum of three numbers(complete the following code)

a=12
b=9
c=15

maximum_num = 0

if a > b and a > c:
    maximum_num = a
if b > a and b > c:
    maximum_num = b
if c > a and c > b:
    maximum_num = c


print(maximum_num, "is the maximum of three numbers.")
print()
#7 a program to check if a character is a vowel or consonant (use if,else & in operator)

character = 'r'
if character in 'aeiou':
    print(character, "is a vowel")
else:
    print(character, "is a consonant")
print()
#8 a program to check if a string is empty or not

string = "Naledi"
if not string:
    print("is empty")
else:
    print("is not empty ")
print()   
#9 a program to check if a string contains a specific substring

mainstring = "Hello World"
substring = "World"

if  substring in mainstring:
    print(f"contains a substring {substring}")
else:
    print(f"does not contain the substring {substring}")
print()
#10 a program to find the maximum of three numbers by taking input from the user(hint)
""" -initialize a variable called max_num = 0
    -create 3 multiline inputs to ask for first, second, third number
    -use,if, elif, else to check those conditions
    -print the result"""
    
max_num = 0

num1=int(input("enter a 1st number: "))
num2=int(input("enter a 2nd number: "))
num3=int(input("enter a 3rd number: "))

if num1 >= num2 and num1 >= num3:
    max_num =num1
elif num2 >= num1 and num2 >= num3:
    max_num =num2
else:
    max_num =num3
    
print(f"the maximum number of three numbers is: {max_num}")
print()
#11 a program to replace a substring in a string and print the updated string (use the .replace)

main_string="Hello World"
new_string=main_string.replace("World", "NaleLulu")
print(new_string)

#12Calulator


