# Name: Ola B.
# Email: code@olab.dev
# Exercise 2 of Week 3

# Creating a list; note the use of commas & the []s
states = ["Washington", "Oregon", "California"]

# Iterating through a list
for state in states:
    print(state)

# Iterating through a list with modification of each index
for state in states:
    state = state.lower()
    print(state)

# Finding out whether an item exists in a list with *in* keyword
print("Washington" in states)
print("Tennessee" in states)
print("Washington" not in states)

# Combining lists together (Concatenation)
states2 = ["Arizona", "Ohio", "Lousisana", "Maryland"]
best_states = states + states2
print(best_states)

# Slicing certain values from a list (Slicing Notation)
print(best_states[1:3])  # only collect from a certain index to a certain index
print(best_states[:2])  # Only collect list items before a certain index
print(best_states[::-1])  # Reverse the list
print(best_states[4:])  # Only collect list items after a certain index
