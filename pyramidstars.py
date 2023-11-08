#prints a triangle with asteriks symbols
print("Print triangle - Pyramind using stars")
size = 7
m = (2 * size) -2
for i in range(0, size):
    for j in range(0, m):
        print(end="")
    m = m - 1
    for j in range(0,i +1):
        print("* ",end='')
    print("")

# prints a square
side = int(input("Please enter any side of a Square: "))
print("Square Star Pattern")
for i in range(side):
    for i in range(side):
        print('*', end= ' ')
    print()