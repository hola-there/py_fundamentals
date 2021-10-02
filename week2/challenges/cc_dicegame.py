# Name: Ola B.
# Email: code@olab.dev
# Challenge 6 of Week 2
import random

# variables initalized
high_score = 0
continue_game = True


# Can provide the result of a dice roll on a dice however large
def dice_rolled(x, y):
    random_dice_face = random.randint(x, y)
    global high_score
    high_score += random_dice_face
    return print("You roll a... " + str(random_dice_face))


# Prints out what occurs from a dice roll; given the number of rolls to enact
def roll_dice(num):
    for i in range(0, num, 1):
        dice_rolled(1, 6)


# Contains the prompts for the game
def dice_game_prompt():
    print("Current High Score:", high_score)
    print("What would you like to do?: ")
    print("1) Roll Dice")
    print("2) Leave Game")
    return input("Enter your choice: ")


def choice_checked(num):
    if num == str(1):
        print()
        roll_dice(2)
        print()
        dice_game()
    elif num == str(2):
        print()
        print("Game Over! Your High Score was: " +
              str(high_score) + ". Come play again some day!")
        global continue_game
        continue_game = False
    else:
        print()
        print("The choice you specified is not an option")
        print("--------------------------")
        print()
        dice_game()


# Game dynamics and setup occurs here
def dice_game():
    choice = dice_game_prompt()
    choice_checked(choice)


# How the actual game runs
while continue_game:
    print()
    print("Welcome to the Dice Game!")
    print()
    dice_game()
