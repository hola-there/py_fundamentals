# Name: Ola B.
# Email: code@olab.dev
# Exercise 5 of Week 2

# Variables declared in a function exist only inside that function
def Seattle():
    dogs = 10000
    print('Seattle has', dogs, 'dogs.')
# When a function call ends the variable is deleted


# This declartion of 'dogs' is within the global not local scope
dogs = "Dogs there are no dogs"


def Bellevue():
    dogs = 2000
    print('Bellevue has', dogs, 'dogs.')


def mess_with_global_var():
    global dogs  # must be declared before any global variable modifications
    dogs = 3000
    dogs = "There are dogs; actually " + str(dogs) + " dogs in fact!"
    print(dogs)


Seattle()
print(dogs)
Bellevue()
mess_with_global_var()
