# Name: Ola B.
# Email: code@olab.dev
# Challenge 1 of Week 4

'''
# Capitalize the first letter of an object name in python
# The blueprint of a object to come
class Player:
    max_hp = 4000  # this is a class attribute

# Instantiating the object
# actually creating something from a class: following through on the blueprint
player1 = Player()
# Access a class's attribute with dot notation
print(player1.max_hp)
player2 = Player()
print(player2.max_hp)

# modifying the class attribute which also changes the objects created of the object
Player.max_hp = 5000
print(player1.max_hp)
print(player2.max_hp)
'''

# start of using the instance attribute


class Player:
    # constructor method must have a parameter list; self is required
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp  # dynamic class instance attribute
        self.score = 0


# Python makes sure that the reference to the object is passed
# which is why self doesn't need to be specified
player1 = Player("Aaron", 1200)
player2 = Player("Irene", 1300)

player1.hp += 500
player1.score += 10
print("P1:", player1.name, " -- HP: ", player1.hp, " -- SCORE: ", player1.score)
print("P2:", player2.name, " -- HP: ", player2.hp, " -- SCORE: ", player2.score)
