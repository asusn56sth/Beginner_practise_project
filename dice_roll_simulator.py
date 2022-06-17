# DICE SIMULATOR

import random

dice = (1, 2, 3, 4, 5, 6)


# randomly select a elements from a sequence
def normal_dice():
    return random.choice(dice)


# get the name of the player
player_name = input("Enter Your name : ")
play = input("Enter to roll the dice: ")
value = normal_dice()
print(f"{player_name} : ", value)


# continous loop to play untill the player enter no.
play = input("Do you want to roll the dice again? (Y/N): ")
game_play = True
while game_play:
    if play == "Y" or play == "y":
        value = normal_dice()
        print(f"{player_name} : ", value)
        play = input("Do you want to roll the dice again? (Y/N): ")
    elif play == "N" or play == "n":
        print(f"Thank you for playing. {player_name}")
        game_play = False
    else:
        play = input("Enter Y/N :")
