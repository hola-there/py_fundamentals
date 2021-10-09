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
# overwriting preexisting key-value pair
state_capitals["Washington"] = "Aberdeen"
state_capitals["Texas"] = "Austin"  # creating/adding a new key-value pair
# printing latest dictionary tied state_capitals dictionary object
print(state_capitals)
print(type(state_capitals))

# Deleting a key-value pair
del state_capitals["California"]  # one method of deleting a key-value pair
# printing latest dictionary tied state_capitals dictionary object
print(state_capitals)
# another method of deleting a key-value pair;
removed_captial = state_capitals.pop("Oregon")
# that will return the value being "popped off"/removed
print(state_capitals)
print(removed_captial)
