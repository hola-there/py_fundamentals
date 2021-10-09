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
