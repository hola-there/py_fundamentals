# Creating variables for characters: Declared the three variables & I set each of their values to a String with their display name
wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50

# Starting the game

while True:
    print("-----------------------------------")
    print("\nWelcome to the Fantasy BattleGame!")
    print()
    print("Here are your character choices: ")
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    character = input("Choose your character: ")
    if character == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Unknown Character")

print("You have chosen the character " + str(character) + "\nHealth: " + str(my_hp) + "\nDamage: " + str(my_damage))