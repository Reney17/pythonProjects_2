
def location1():
 DefLocation=["Default"]

replacement=input("Enter the value to replace:     ")
indextoreplace=DefLocation.index(replacement)

newvalue=input("Enter new value:   ")

DefLocation[indextoreplace]=newvalue

#print(newvalue)

print(DefLocation[0])