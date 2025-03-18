"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                GUESSING GAME
---------------------------------------------------------------------------------
- File Name: to-do-list.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Complete a functional dice roller app in Python.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Tasks = []
def get_number(message):
    while True:
        bob = input(f"{message}: ")
        try:
            return(int(bob))
        except ValueError:
            print("The number you entered isn't valid.")

def view_list(list):
    for i, x in enumerate(list):
        print(f"{i}. {x}")

def add_task(list):
    while True:
        newtask = input("Add a task: ")
        confirm = input("Would you like to confirm? Y/N: ")
        if(confirm == "Y" or  confirm == "y"):
            list.append(newtask)
            print("This is the updated list:")
            view_list(list)
            return

def remove_task(list):
    while True:
        view_list(list)
        removeindex = get_number("Which number on your list would you like to remove?")
        confirm = input("Would you like to confirm? Y/N: ")
        if(confirm == "Y" or  confirm == "y"):
            list.pop(removeindex)
            print("This is the updated list:")
            view_list(list)
            return  
        
def mark_task(list):
    while True:
        view_list(list)
        markindex = get_number("Which number on your list would you like to mark as done?")
        confirm = input("Would you like to confirm? Y/N: ")
        if(confirm == "Y" or  confirm == "y"):
            list[markindex] = "//" + list[markindex]
            print("This is the updated list:")
            view_list(list)
            return  
def edit_task(list):
    while True:
        view_list(list)
        editindex = get_number("Which number on your list would you like to mark as done?")
        confirm = input("Would you like to confirm? Y/N: ")
        if(confirm == "Y" or  confirm == "y"):
            list[editindex] = input("Type in your edited task: ")
            print("This is the updated list:")
            view_list(list)
            return  
        
def search_task(list):
    view_list(list)
    search = input("What would you like to search?: ")
    if search in list:
        print(f"{search} is in your list, number: {list.index(search)}")
        return
    else:
        print(f"{search} is not in your list")
        return

def menu():
    optionsstr = ["View the list", "Add a new task", "Remove a task", "Mark a task as done", "Edit a task", "Search for a task"]
    for i, x in enumerate(optionsstr):
        print(f"{i}. {x}")
    while True:
            input = get_number("What would you like to do?")
            if input == 0:
                view_list(Tasks)
                return
            elif input == 1:
                add_task(Tasks)
                return
            elif input == 2:
                remove_task(Tasks)
                return
            elif input == 3:
                mark_task(Tasks)
                return
            elif input == 4:
                edit_task(Tasks)
                return
            elif input == 5:
                search_task(Tasks)
                return
            else:
                print("Invalid")
    
while True:
    menu()
    confirm = input("Would you like to go again? Y/N: ")
    if(confirm != "Y" and confirm != "y"):
        break