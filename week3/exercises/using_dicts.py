# Name: Ola B.
# Email: code@olab.dev
# Exercise 4 of Week 3

# Creation of a dictionary
state_capitals = {"Washington": "Olympia",
                  "Oregon": "Salem", "California": "Sacramento"}
# print(len(state_capitals)) # Length of the dictionary according to the # of key:value pairs

# Accessing dictionary values
# print(state_capitals["Washington"]) # Printed the value tied to the key 'Washington'

# Modifying/adding key-value pairs
# overwriting preexisting key-value pair
state_capitals["Washington"] = "Aberdeen"
# creating/adding a new key-value pair
state_capitals["Texas"] = "Austin"
# printing latest dictionary tied state_capitals dictionary object
print(state_capitals)
print(type(state_capitals))
