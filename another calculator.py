# Define functions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Display menu options to the user
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get the user's choice
choice = input("Enter choice (1/2/3/4): ")

# Get input numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the selected operation
if choice == '1':
    result = add(num1, num2)
    print("Result:", result)
elif choice == '2':
    result = subtract(num1, num2)
    print("Result:", result)
elif choice == '3':
    result = multiply(num1, num2)
    print("Result:", result)
elif choice == '4':
    result = divide(num1, num2)
    print("Result:", result)
else:
    print("Invalid input")
