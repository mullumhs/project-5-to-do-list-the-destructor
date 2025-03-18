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
        if(confirm == "Y" or "y"):
            list.append(newtask)
            view_list(list)
            return

def remove_task(list):
    while True:
        view_list(list)
        removeindex = get_number("Which number on your list would you like to remove?")
        confirm = input("Would you like to confirm? Y/N: ")
        if(confirm == "Y" or "y"):
            list.pop(removeindex)
            view_list(list)
            return  
        
def menu():
    optionsstr = ["View the list", "Add a new task", "Remove a task"]
    for i, x in enumerate(optionsstr):
        print(f"{i}. {x}")
    
    input = get_number("What would you like to do?")
    if input == 0:
        view_list(Tasks)
    elif input == 1:
        add_task(Tasks)
    elif input == 2:
        remove_task(Tasks)
    
    
menu()