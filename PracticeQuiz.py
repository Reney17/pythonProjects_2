# p, q, r = 10, 20 ,30
# print(p, q, r)

# var = "James" * 2  * 3
# print(var)

# for x in range(0.5, 5.5, 0.5):
#   print(x)
  
# sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add(1, "Vicki")
# print(sampleSet)

# str = "pynative"
# print (str[1:3])

# for i in range(10, 15, 1):
#   print( i, end=', ')
  
# sampleList = ["Jon", "Kelly", "Jessa"]
# sampleList.append(2, "Scott")
# print(sampleList)

# def calculate (num1, num2=4):
#   res = num1 * num2
#   print(res)

# calculate(5, 6)

# x = 50
# def fun1():
#     x = 25
#     print(x)
    
# fun1()
# print(x)

# st ='python strings'
# print(st[-14:-8])

# st ='python strings'
# print(st[-14:-6])

# name = "Micheal"
# print(name.upper())
# print()
# name = "Micheal"
# print(name.lower())
# print()
# name = "Micheal"
# print(name.capitalize())
# print()
# name = "Micheal"
# print(name.find('h'))
# print()
# name = "Micheal"
# print(name.replace("Micheal", "John"))
# print()
# name = "Micheal"
# if 'h' in name:
#     print("True")
# else:
#     print("False")
# print()   
# name = "Micheal"
# letter='h'in name
# print(letter)
# print()

    
# name = "Micheal"
# print(name.strip())



# x = 50
# def fun1():
#     x = 25
#     print(x)
    
# fun1()
# print(x)

# print(type([]) is list)

# print(type(10))

# print(type(0xFF))

# print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))

# x = 50
# def fun1():
#     global x
# x = 20
#        # your code to assign global x = 20
# fun1()
# print(x) # it should print 20

# type(range(5))


# print(36/4)

# name = "python\'s operators "
# word ="is nice"
# print(name)
# print(word)



# Write a python program to add two int number from a user and returns the result as float number/output 
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# sum=float(num1+num2)
# print(f"The result is: {sum}")

#python program to find the max of two numbers from the user.You can use values entered
# num1=float(input("Enter first number: "))
# num2=float(input("Enter second number: "))
# max_num=max(num1, num2)
# print(f"The maximum number is: {max_num}")

#Initialize the biggest number of your choice to a variable
# """-let the user input a value once
# -use an if statement to check if the number entered is greater or less than your selected number choice
# - then if it is greater than the new number has to replace that selected number choice
# - then prompts the user again for a number 
# - finally prints the largest number"""

# biggest_num = 100
# selected_num =int(input("Enter any number:  "))
# while True:
#     if selected_num > biggest_num:
#         biggest_num = selected_num
#         print(f"The selected number has been updated to {biggest_num}")
#         # break
#         selected_num =int(input("Enter any number:  "))
#     elif selected_num < biggest_num:
#         print("The number you have selected is less that the biggest number")
#         selected_num=int(input("Enter any number:  "))
#     elif selected_num == biggest_num:
#         print("the number you selected is the same as the biggest number")
#         selected_num =int(input("Enter any number:  "))
#     else:
#         print("invalid selection!")
#         break
# print(f"The largest number entered is: {biggest_num}")

# start = input("How old were you on your start date? ")
# end = input("How old are you today? ")


# print("Congratulations on" + str(int(end)-int(start)) + "years of service!")

# a = 11
# b = 4

# print(a/b)
# print(a%b)
# print(a//b)


# print((3*(1+2)**2 - (2**2)*3))

# x1 = "20"
# y1 = 3
# a = x1 * y1

# b = "Hello, World!"
# print(b[-5:-2])

# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))



# a = "BMW" 
# b = "powerful" 
# c = "makes" 
# d = "cars" 
# str = '{0} {2} {1} {3}'.format(a, b, c, d) 
# print(str)

# list1 = [1, 2]
# list2 = [3, 4]
# list_3 = list1 + list2
# list_4 = list_3 * 3
# print(list_4)

# rooms = {1: 'Foyer', 2: 'Conference Room'}
# room = input("Enter the room number:")
# if not room in rooms:
#     print('Room does not exist.')
# else:
#      print("The room name is " + rooms[room])
# def show_summary(name: int, age: int) -> str:
    
#     #get summary of this person 
#     summary =name + "is" + str(age)
# your_name ="Bob"
# your_age = 21

# final_text =show_summary(your_age,your_age)
# print(final_text)

# import sys
