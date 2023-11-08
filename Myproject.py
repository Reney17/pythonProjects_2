#Question1-Eggs pricing Calculator
""" a program that prompts the user for the number of eggs they wish
to order and calculates the total amount owed, along with a detailed breakdown of the order."""

# Pricing options

Price_egg_dozen = 3.25
Price_loose_egg = 0.45

#A program that will prompt user input


Number_of_eggs = int(input("Please enter number of eggs you wish to order: "))

Num_egg_dozen = Number_of_eggs // 12
print(Num_egg_dozen)

individual_eggs = Number_of_eggs % 12

print(individual_eggs)


Total= (Num_egg_dozen*Price_egg_dozen) + (individual_eggs*Price_loose_egg)
print(Total)

#Display the amount owed and order breakdown

print("You ordered",Number_of_eggs,"eggs.","That's",Num_egg_dozen,"dozen at",Price_egg_dozen,"per","number of eggs","and",individual_eggs,"loose eggs at",Price_loose_egg,"for a total of",Total)