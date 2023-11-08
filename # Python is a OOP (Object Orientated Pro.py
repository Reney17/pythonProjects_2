# Python is a OOP (Object Orientated Programming)
# Python objects-used to avoid redundancy and to reusability purposes
# Dictionary works with key value pairs
# Tuples-immutable
# lists-mutable
# types of errors

#1-twinkle twinkle

# print("Twinkle, twinkle, little star,")
# print("     How I wonder what you are!")
# print("         Up above the world so high,")
# print("         Like a diamond in the sky.")
# print("Twinkle, twinkle, little star,")
# print("     How I wonder what you are!")

#2- A python program that calculates the area of a circle based on the radius entered by the user
#get the radius from the user

# radius = float(input("Enter the radius:  "))
# area = 3.14*(radius**2)
# print("area of the circle", area)


#3- A python program that accepts the user's first and last name and prints them in reverse order with a space between them


#4- A python program thats accepts an integer(n)and computes the value of n+nn+nnn. Sample value of n is 5

# num = int(input("Input an integer : "))
# n = int( "%s" % num )
# nn = int( "%s%s" % (num,num) )
# nnn = int( "%s%s%s" % (num,num,num) )
# print (n+nn+nnn)

#5-A python program to sum three given integers.However ,if two values are equal ,the sum will be zero

#initializing of values
a = int(input("Enter Value 1 : "))
b = int(input("Enter Value 2 : "))
c = int(input("Enter Value 3 : "))
#Using the if loop
if a == b or b==c or c==a:
    print("Sum is : 0")
else:
    d = a + b + c
    print("Sum is : ",d)
    


#6-A Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
#defining a function
def sum(x, y):
    sum = x + y
#if loop 
    if sum in range(15, 20):
        return 20
    else:
        return sum
#print statements
print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))


#7- A Python program that returns true if the two given integer values are equal or their sum or difference is 5

