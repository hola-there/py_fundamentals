# Name: Ola B.
# Email: code@olab.dev
# Challenge 2 of Week 3

# Our string to work with
MY_STRING = "giraffe"

# First example printing the last character in the string provided
print("Output of 'my_string[-1]' is: " + MY_STRING[-1])
# Equivalent to my_string[6]
'''
                                       |
   0  |  1  |  2  |  3  |  4  |  5  |  6
-------------------------------------------
|  g  |  i  |  r  |  a  |  f  |  f  |  e  |
-------------------------------------------
  -7  | -6  | -5  | -4  | -3  | -2  | -1
                                       |
'''

# Second example printing characters starting from index 2 up to index 3 \
# (does not include the index after the colon)
print("Output of 'my_string[2:4]' is: " + MY_STRING[2:4])
# So from index 2 to index 3 since the stop is not inclusive but the start position is
# Equivalent to my_string[-5:-3]
'''
               | --> |
   0  |  1  |  2  |  3  |  4  |  5  |  6
-------------------------------------------
|  g  |  i  |  r  |  a  |  f  |  f  |  e  |
-------------------------------------------
  -7  | -6  | -5  | -4  | -3  | -2  | -1
               | --> |
'''

# This example is useful if you think that the mutable list will change at some point
print("Output of 'my_string[:]' is: " + MY_STRING[:])
# Basically the same as my_string[0:len(my_string)] or my_string
'''
   | --> | --> | --> | --> | --> | --> |
   0  |  1  |  2  |  3  |  4  |  5  |  6
-------------------------------------------
|  g  |  i  |  r  |  a  |  f  |  f  |  e  |
-------------------------------------------
  -7  | -6  | -5  | -4  | -3  | -2  | -1
   | --> | --> | --> | --> | --> | --> |
'''

# Example of slicing from a certain point onwards but from the end of the list
print("Output of 'my_string[:-2]' is: " + MY_STRING[:-2])
# Equivalent to my_string[5]
'''
                                 |
   0  |  1  |  2  |  3  |  4  |  5  |  6
-------------------------------------------
|  g  |  i  |  r  |  a  |  f  |  f  |  e  |
-------------------------------------------
  -7  | -6  | -5  | -4  | -3  | -2  | -1
                                 |
'''

# Example of slicing from a certain point onwards but from the end of the list
print("Output of 'my_string[-4:-1]' is: " + MY_STRING[-4:-1])
# So from index -4 to index -2 since the stop is not inclusive but the start position is
# Equivalent to my_string[3:5]
'''
                     | --> | --> |
   0  |  1  |  2  |  3  |  4  |  5  |  6
-------------------------------------------
|  g  |  i  |  r  |  a  |  f  |  f  |  e  |
-------------------------------------------
  -7  | -6  | -5  | -4  | -3  | -2  | -1
                     | --> | --> |
'''
# When you use sliciing notation without specifying start nor end you'll end up
# with a reversed output of the provided indexed sequence
print("Output of 'my_string[::-1]' is: " + MY_STRING[::-1])
print("Output of 'my_string[-1:(-1 * (len(my_string) + 1)):-1]' is: " +
      MY_STRING[-1:(-1 * (len(MY_STRING) + 1)):-1])
print("Output of 'my_string[len(my_string)::-1]' is: " +
      MY_STRING[len(MY_STRING)::-1])
# Basically print everything but backwards
# Equivalent to my_string[-1:(-1 * (len(my_string) + 1)):-1]
# Also equivalent to my_string[(len(my_string):0:-1]
'''
   | <-- | <-- | <-- | <-- | <-- | <-- |
   0  |  1  |  2  |  3  |  4  |  5  |  6
-------------------------------------------
|  g  |  i  |  r  |  a  |  f  |  f  |  e  |
-------------------------------------------
  -7  | -6  | -5  | -4  | -3  | -2  | -1
   | <-- | <-- | <-- | <-- | <-- | <-- |
'''

# When you use sliciing notation with a negative step a the start and stop must also be backward
print("Output of 'my_string[6:1:-2]' is: " + MY_STRING[6:1:-2])
print("Output of 'my_string[-1:-6:-2]' is: " + MY_STRING[-1:-6:-2])
# Basically print everything within the range but every 2 steps not every single step
# Equivalent to my_string[-1:-6:-2]
'''
               | <--   <-- | <--   <-- |
   0  |  1  |  2  |  3  |  4  |  5  |  6
-------------------------------------------
|  g  |  i  |  r  |  a  |  f  |  f  |  e  |
-------------------------------------------
  -7  | -6  | -5  | -4  | -3  | -2  | -1
               | <--  <--  | <--   <-- |
'''

# Other useful links:
# https://docs.python.org/3.9/library/stdtypes.html#common-sequence-operations
# https://www.w3schools.com/python/ref_func_slice.asp
# https://realpython.com/lessons/indexing-and-slicing/
# https://discuss.codecademy.com/t/negative-slicing-python/492986
# https://stackoverflow.com/questions/493046/i-dont-understand-slicing-with-negative-bounds-in-python-how-is-this-supposed
