"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Work some of the more advanced features of lists in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Here is a list of 10 fruits:
fruits = ["Grape", "Apple", "Lemon", "Cherry", "Date", "Elderberry", "Fig",  "Honeydew", "Kiwi", "Banana"]


# Remove the third fruit from the list using the pop() method.
fruits.pop(2)

# Use the remove() method to remove a fruit of your choice from the list.
fruits.remove("Fig")

# Search for "Apple" in the list and print a message saying whether or not it was found.
if "Apple" in fruits:
    print("Apple is in list.")

# Sort the List in alphabetical order.
fruits.sort()

# Create a new list that contains a slice of the first 5 items
newfruits = fruits[0:5]

# Print out the new sliced list using a for loop
for i in newfruits:
    print(i)