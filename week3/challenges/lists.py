# Name: Ola B.
# Email: code@olab.dev
# Challenge 1 of Week 3

import random

diamonds = ["AD", "2D", "3D", "4D", "5D",
            "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

player_hand = []


# Gets a hand from the subset of cards provided and adds it to the player's hand
def get_new_hand():
    random_card = random.randint(0, (len(diamonds) - 1))
    player_hand.append(diamonds[random_card])
    diamonds.pop(random_card)


def print_deck(deck_name, deck):
    print("The contents of '" + str(deck_name) + "' is: " + str(deck))


while diamonds:
    user_choice = input(
        "Press enter to pick a card; or 'Q' then enter to quit: ")
    if user_choice.upper() == "Q":
        print("Exiting now...!")
        break
    get_new_hand()
    print_deck("Diamonds deck", diamonds)
    print_deck("Player deck", player_hand)
    if not diamonds:
        print("There are no more cards to pick.")
