# Name: Ola B.
# Email: code@olab.dev
# Exercise 4 of Week 2

def myFn():
    print("You have called my function")


def add(x, y):
    z = x + y
    print(z)


def subtract_nums(x, y):
    z = x - y
    return str(x) + " subtracted by " + str(y) + " is " + str(z)


myFn()
add(2, 3)
add(3, 4)
a = 4
b = 5
add(a, b)
print(subtract_nums(5, 2))
