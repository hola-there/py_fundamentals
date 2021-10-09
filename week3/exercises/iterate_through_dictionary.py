# Name: Ola B.
# Email: code@olab.dev
# Exercise 5 of Week 3

# Creation of a dictionary
state_capitals = {"Washington": "Olympia",
                  "Oregon": "Salem", "California": "Sacramento"}

# Iterating through keys the dictionary
'''for state in state_capitals:
    print(state)'''

# Iterating through values in the dictionary
'''for city in state_capitals.values():
    print(city)'''

# Iterating through both keys and values with bracket notation
for state in state_capitals:
    print(state_capitals[state], "is the capital of", state)

print()

# Iterating through both keys and values with dict itmes
for state, city in state_capitals.items():
    print(city, "is the capital of", state)
