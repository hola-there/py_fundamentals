# Name: Ola B.
# Email: code@olab.dev
# Exercise 7 of Week 2

# Creating the fibonacci sequence; code that will get the number in the
# Fibonacci seqeunce will be provided

import sys

program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)

for x in sys.argv:
    print("Argument: ", x)


def rFib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return rFib(n-1) + rFib(n-2)


print(rFib(int(sys.argv[1])))
