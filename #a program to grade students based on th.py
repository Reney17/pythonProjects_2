#a program to grade students based on the marks by taking user input

#Marks for students
Score = 85
Score = 90
Score = 80

#User input

marks = int(input("Enter student marks: "))

#Conditional statements
while True:
    
    if marks >= 90:
        print("Grade: A")
        marks = int(input("Enter student marks: "))
    elif marks >=80 and marks <89:
        print("Grade: B")
        marks = int(input("Enter student marks: "))
    else:
        marks <80
        print("Grade: 0")
        print("Your entered mark is:  ",marks,"which is","out of criteria")
    break
    
    
    
    