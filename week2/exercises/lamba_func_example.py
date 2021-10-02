# Name: Ola B.
# Email: code@olab.dev
# Exercise 6 of Week 2

'''
Showcasing an example of an anonymus function(does not have a name)
used when a function doesn't need a name nor needs to be held in memory for later use
'''

# lambda syntax layout
'''
Arugement is comma-seperated, not surrounded by parentheses
Multiple Arguments allowed
Only one expression/line allowed in function body
'''
# lambda arg1, arg2: expression to return
lambda num: num ** 2

# the lamba setup as a function


def square(num):
    return num ** 2

# Lambda function callback example
# This higher-order function has a parameter of a callback function


def a_function(callback):
    print(callback(3))


# This calls the higher-order function with a lambda functino argument
a_function(lambda num: num ** 2)  # this should print 9
