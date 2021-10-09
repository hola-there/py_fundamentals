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

# Trying out set values
# numbers_set = {1, 2, 3, 4, 4} # duplicate values removed
# numbers_set = {1, 2, 3, 4, [5, 6]}  # cannot use mutable data types in a set
# numbers_set = {1, 2, 3, 4, (5, 6)}  # tuples are immutable so this is a okay
# print(numbers_set)

# accessing set values
words_set = {"Alpha", "Bravo", "Charlie"}

abcd = ""
for word in words_set:
    abcd += word
# sets are unordered so the order of the items aren't set. different values per run
print(abcd)
