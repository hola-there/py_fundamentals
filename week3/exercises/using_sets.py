# Name: Ola B.
# Email: code@olab.dev
# Exercise 8 of Week 3

# sets are an unordered collection of balues
# sets are comma seperated
# sets are not indexed..so no bracket notation
# sets are mutable but cannot contain mutable data types
# sets automagically removes duplicates
# sets can be created empty with the set() function

# Creating an empty set
empty_set = set()

# numbers_set = {1, 2, 3, 4, 4} # duplicate values removed
# numbers_set = {1, 2, 3, 4, [5, 6]}  # cannot use mutable data types in a set
numbers_set = {1, 2, 3, 4, (5, 6)}
print(numbers_set)
