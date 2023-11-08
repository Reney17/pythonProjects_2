#Multiplication game
"""A program that allows the user to play a multiplication game. At the beginning of each round, the program
randomly selects two numbers from 1 to 10, displays the chosen numbers, and prompts the player to calculate the
product of both numbers. If the player correctly answers the question, the program asks if they want to continue
playing. This cycle continues until the player makes a mistake or chooses to end the game"""

import random
playerChoice = 'y'
counter = 0

#defines product
def product(valueOne, valueTwo):
    return valueOne * valueTwo

#loop to continue the game
while playerChoice == 'y': 
    firstValue = random.randrange(0,11)
    secondValue = random.randrange(0,11)
    print(f"What is the product of {firstValue} and {secondValue} = ")
    thirdValue = int(input())

#manual entry
    #firstValue = int(input("Enter the first value: "))
    #secondValue = int(input("Enter the second value: "))
    #thirdValue = int(input("Enter the product of your chosen values: "))

#compares user input vs the actual product
#then counter goes up if it is correct else ends the program
    if thirdValue == product(firstValue, secondValue):
        playerChoice = (str(input("That is correct!\nDo you want to play again? (y/n)")))
        counter += 1
    else: 
        print(f"That was not the correct guess!\nThe correct product was {product(firstValue, secondValue)}.")
        playerChoice = 'n'

    if playerChoice.lower() == 'n':
        playerChoice = 'n'
        
#prints number of correct guesses made
print("\nThe correct number of guesses made were: ", counter)