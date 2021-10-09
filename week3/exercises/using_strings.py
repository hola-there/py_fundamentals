# Name: Ola B.
# Email: code@olab.dev
# Exercise 3 of Week 3

MY_STRING = "alpha"
'''multiline_string = """bravo
charlie"""
print(my_string)
print(multiline_string)'''

# Printing a certain index of a string since it is a indexed sequence
'''
print(MY_STRING[0])
print(MY_STRING[3])
'''

# Slicing Notation of a String
print(MY_STRING[0:3])
print(MY_STRING[:2])
print(MY_STRING[2:])
print(MY_STRING)

# Iterate through a string
for char in MY_STRING:
    print(char)

# Test substring existence in a string
print("pha" in MY_STRING)
print("z" not in MY_STRING)
