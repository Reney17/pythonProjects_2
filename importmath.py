#   a python program to find the area of a triangle whose sides are given(1)
# import math

# # Assign values to  a, b, c and s

# a = int(input("Enter the length of side b:  "))
# b = int(input("Enter the length of side c:  "))
# c = int(input("Enter the length of side d:  "))
# s = (a + b + c)/2

# #   Calculate the area and round off the result to 2 decimal places
# area = round(math.sqrt(s*(s-a)*(s-b)*(s-c)), 2)

# print("Area:", area)

# #  python on program to find out the average of a set of integers(2)
# list = [3, 5, 6, 7, 4, 7]


# l=[]
# count = int(input("Please enter a count of all numbers:  "))
# i = 0
# sum = list
# for i in range(count):
#     x = int(input("Enter a number:  "))
#     break
# sum = sum + x
# avg = sum/count
# print("The average is:  ,avg")

while True:
    l=[]
    print("A PROGRAM TO CALCULATE THE AVERAGE OF INTEGERS ENTERED BY THE USER")
    number = int(input("Please enter integers  "))
    l.append(number)
    ques=input("Do you want to continue: Y/N ")
    
    while ques == 'Y' or ques =='y':
       
        num2 = int(input("Please enter a count of all numbers:  "))
        l.append(num2)
        print(l)
        ques=input("Do you want to continue: Y/N ")
    if ques == 'N' or ques =='n':
        print("sum of the list is :",sum(l))
        avg = sum(l)/len(l)
        print("average of :",l,"is :",avg.__round__(2))
        break
    





#  Python program to find the product of a set of real numbers(3)






#   happy birthday song program

# name =input("Who's birthday is it today?:  ")

# print(f"Happy birthday to you..\nHappy birthday to you..\n Happy birthday dear, {name}\n Happy birthday to you")



# list = [3, 5, 6, 7, 4, 7]
# agree = "Y"
# Disagree= "N"

# while True:
    
#     l=[]
#     count = int(input("Please enter a count of all numbers:  "))
#     l.append(l)
#     ques=input("Do you want to continue: Y/N ")
#     if ques==agree: # if ques.startswith ='Y' or ques.startswith='y'
#         count = int(input("Please enter a count of all numbers:"))
#         l.append(l)
       
#     elif ques==Disagree: # if ques.startswith ='N' or ques.startswith='n'
#         print(sum(l))
#         break
#     else:
#         print("You did not enter in a character")
#         ques=input("Do you want to continue: Y/N ")
        
        
      
        
    




# i = 0
# sum = list
# for i in range(count):
#     x = int(input("Enter a number:  "))
#     break
# sum = sum + x
# avg = sum/count
# print("The average is:  ,avg")

