#to do app

def add_todo_item():
    global todo_list
    new_item =input("Enter a new TODO Item: ")
    todo_list.append(new_item)
    print("Item Added successfully", end= '\n\n')

print("Todo do app".center(25, '-'))

todo_list=[]


while True:
    print("1. ADD TODO",
          "2. EDIT TODO",
          "3. REMOVE TODO ITEM",
          "4. BULK ADD",
          "5. VIEW ALL",
          "6. EXI",
          sep='\n',
          end='\n\n')
    
    choice =int(input("Enter your choice: "))
    
    #IF ELSE STATEMENTS TO HANDLE USERS
    if choice ==1:
        #add a new todo_item to the list
        new_item=input("Enter a new TODO Item: ")
        todo_list.append(new_item)
        print("Item added successfully 😊 ", end='\n\n')
    if choice == 5:
        #view todo items
        print("TODO LIST ITEMS".center(25, '-'))
        for todo_item in add_todo_item:
            print(todo_item)
        print()
    if choice==6:
        break


print("Goodbye!".center(25, '-'))


def add_todo_item():
    global todo_list
    new_item = input("Enter a")