#QUESTION3: Multiplication game

"""A program that allows the user to play a multiplication game. At the beginning of each round, the program
randomly selects two numbers from 1 to 10, displays the chosen numbers, and prompts the player to calculate the
product of both numbers. If the player correctly answers the question, the program asks if they want to continue
playing. This cycle continues until the player makes a mistake or chooses to end the game"""

import random
#----------------user functions-------------------------------#
# generating any random numbers between 1 and 10
def gen_random_nums():
    num1 = random.randit(1, 10)
    num2 = random.randit(1, 10)
    return num1, num2

#user input after prompting for an answer
def prompt_for_answer(num1, num2):
    user_answer = int(input(f"What is {num1} x {num2}?  "))
    return user_answer

#functionality to check if the answer given by the user is correct
def check_answer(num1, num2, user_answer):
    correct_answer = num1 * num2
    return user_answer == correct_answer

#functionality for player to start the game and give score
def start_game():
    score = 0
    play_again = 'y'
    
 #Display when starting the game   
    print("Let's play a multiplication game!")
 #while loop to allow user to play the game again   
    while play_again.lower() == 'y':
        num1, num2 = gen_random_nums()
        user_answer = prompt_for_answer(num1, num2)
        
        if check_answer(num1, num2, user_answer):
            score +=1
            print(f"Correct! Your score is {score}")
        else:
            print(f"Wrong answer! Your final score is {score}")
            break
        
        play_again = input("Do you want to play again? (y/n)   ")
        
    print("Thanks for playing!")
    
#call the play_game function to start the game
start_game()

    
    
    
    