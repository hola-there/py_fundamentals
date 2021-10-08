# Name: Ola B.
# Email: code@olab.dev
# Workshop #1 from Week 1

# Obtaining any modules needed
from math import fabs  # Source: https://www.w3schools.com/python/ref_math_fabs.asp
import random  # Source: https://docs.python.org/3/library/random.html

# Declaring functions


# Helps print an empty new line
def add_empty_line():
    print("")


# Used to provide a random number between the specified range for this program
def get_random_num():
    # Source for random function: https://docs.python.org/3/library/random.html#random.randint
    return random.randint(2, 7)


# Used python's setup for a case/switch statement for different/random character attack info
def character_attack_information(argument):
    new_switcher = {
        1: "The " + str(character) + " meets a dragon & attacks with a quick blow",
        2: "The " + str(character) + " attempts to deal a fatal blow to the dragon",
        3: "The " + str(character) + " merely scraches the dragon",
        4: "The " + str(character) + " hits a solid blow on the dragon",
        5: "The " + str(character) + " deftly attacks the dragon with a sneak attack",
        6: "The " + str(character) + " damaged the Dragon by " + str(my_damage) + "!"
    }
    return new_switcher.get(argument, "The " + str(character) + " attacks the Dragon!")


# Used python's setup for a case/switch statement for different/random dragon attack info
def dragon_attack_information(argument):
    switcher = {
        1: "The dragon eyes the " + str(character) + ". Makes it somersault and then looks on with hunger & anger in it's eye",
        2: "The dragon hits the " + str(character) + " with a sweltering flame",
        3: "The dragon launches the " + str(character) + " with a gust of air from it's wing",
        4: "The dragon slashes the " + str(character) + " with it's claw",
        5: "The dragon rams into the " + str(character) + " at full speed!",
        6: "The dragon opens it's large jaw & bites the " + str(character) + " just enough to leave teeth marks"
    }
    return switcher.get(argument, "The Dragon strikes back at the " + str(character))


# Starting the game
play_game = True
# Game loop beings
while play_game:
    # Creating variables for characters: Declared the three variables & I set each of their values to a String with their display name
    wizard = "Wizard"
    elf = "Elf"
    human = "Human"
    orc = "Orc"

    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    orc_hp = 200

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    orc_damage = 125

    dragon_hp = 300
    dragon_damage = 50
    # The game output starts iwht choices and an introduction
    while True:
        print("-----------------------------------")
        print("\nWelcome to the Fantasy BattleGame!")
        add_empty_line()
        print("Here are your character choices: ")
        print("1) Wizard")
        print("2) Elf")
        print("3) Human")
        print("4) Orc")
        print("5) Exit")
        add_empty_line()
        player_option = input("Choose your character: ")
        if player_option == "1" or player_option.lower() == "wizard":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif player_option == "2" or player_option.lower() == "elf":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif player_option == "3" or player_option.lower() == "human":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        elif player_option == "4" or player_option.lower() == "orc":
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break
        elif player_option == "5" or player_option.lower() == "exit":
            quit()
        else:
            print("Unknown Character")
    # Character and Dragon attack one another for the first time
    # Source: https://stackoverflow.com/questions/15286401/print-multiple-arguments-in-python
    print("You have chosen the character: " + str(character) +
          "\nHealth: " + str(my_hp) + "\nDamage: " + str(my_damage))
    print("\n" + character_attack_information(1))
    dragon_hp -= my_damage
    print("The dragon's hit points are now: " + str(dragon_hp) + "\n")
    print("" + dragon_attack_information(1))
    my_hp -= dragon_damage
    print("The " + str(character) + "'s hit points are now: " + str(my_hp) + "\n")

    # Source: https://pythonguides.com/increment-and-decrement-operators-in-python/#:~:text=loop%20multiple%20conditions-,Python%20decrement%20operator,-Let%20us%20understand
    # The character and dragon continue atacking one another until one is defeated
    while True:
        print("" + character_attack_information(get_random_num()))
        dragon_hp -= my_damage
        print("The dragon's hit points are now: " + str(dragon_hp) + "\n")
        if dragon_hp <= 0:
            print("The Dragon has lost the battle")
            break
        print("" + dragon_attack_information(get_random_num()))
        my_hp -= dragon_damage
        print("The " + str(character) +
              "'s hit points are now: " + str(my_hp) + "\n")
        if my_hp <= 0:
            print("The " + str(character) + " has lost the battle")
            break
    # it is determined whether a player would like to continue playing the game or not
    while True:
        continue_playing = input(
            "Would you like to continue playing the game? (yes,1,true or no,0,false): ")
        if isinstance(continue_playing, str):
            if continue_playing == "1" or continue_playing == "true" or continue_playing == "yes":
                play_game = True
                break
            elif continue_playing == "0" or continue_playing == "false" or continue_playing == "no":
                play_game = False
                print("Hope you enjoyed the game!\n Goodbye!")
                break
            else:
                print("A valid option was not provided please try again")
