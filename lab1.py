"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and use lists in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a list named favorite_foods and add at least five different food items to it
foods = ["bob", "bob2", "bob3", "bob4", "bob5"]

# Change the third item in the list to a different food
foods[2] = "newbob"

# Print out only the first and fourth items in the list
print(foods[0], foods[3])

# Ask the user for a food item
fooditem = input("What is your fav food?: ")

# Append the user's food item to the list
foods.append(fooditem)

# Print out the entire list of food items
print(foods)