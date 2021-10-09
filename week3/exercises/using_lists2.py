# Name: Ola B.
# Email: code@olab.dev
# Exercise 11 of Week 3

# Creating a list; note the use of commas & the []s
states = ["Washington", "Oregon", "California"]
# Iterating through a list
for x in states:
    print(x)

# Retrieve values in a list
''' 
print(states[-1])
print(states[-2])
print(states[-3])
'''

# Modifying list values
states[2] = "Arizona"
# print(states)

# Finding the length of a list
# print(len(states))

# Testing out List methods (functions that are tied to an object)

# Adding an item to a list with the append list method
states.append("New York")
print(states)

# Removing the last item to a list with the pop list method
states.pop()
print(states)

# Removing a list item from a specific index
states.pop(1)
print(states)
