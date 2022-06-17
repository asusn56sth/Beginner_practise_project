# Customized DICE SIMULATOR

import random

dice = (1, 2, 3, 4, 5, 6)


# select a random choice from a sequence, weight of a specific number is higher so that a number is preferred more than other.
def customized_dice():
    return random.choices(dice, weights=[1, 1, 1, 1, 1, 10], k=1)


# get the player name
player_name = input("Enter Your name : ")
play = input("Press Enter to roll the dice. ")
value = customized_dice()
print(f"{player_name} : ", value[0])

# continuous loop to play untill the player enter no.
play = input("Do you want to roll the dice again (Y/N): ")
game_play = True
while game_play:
    if play == "Y" or play == "y":
        value = customized_dice()
        print(f"{player_name} : ", value[0])
        play = input("Do you want to roll the dice again (Y/N): ")
    elif play == "N" or play == "n":
        print(f"Thank you for playing. {player_name}")
        game_play = False
    else:
        play = input("Enter Y/N :")
