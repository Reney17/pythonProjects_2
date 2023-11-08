import random
Start_game=input("Would you like to play the game? y/n")
if(Start_game=="y"):
    play_again= input("would you like to play")
    while(play_again=="y"):
            
#Initialize random numbers

RandomNumList=[1,2,3,4,5,6,7,8,9,10]

#create a variable to store the first selected random numbers
RandomNumSelector= random.randrange(len(RandomNumList))
RandomNumSelector2= random.randrange(len(RandomNumList))
RandomNum1=RandomNumList[RandomNumSelector]
RandomNum2=RandomNumList[RandomNumSelector2]
Answer=RandomNum1*RandomNum2
UserAnswer=int(input(f"What is the product of {RandomNum1}*{RandomNum2}"))
if(Answer != UserAnswer):
    print("incorrect")
elif(Answer==UserAnswer):
    print("correct")
elif(play_again==n)