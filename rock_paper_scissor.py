# ROCK PAPER ScISSOR

# importing random module to generate ramdom choice
import random
import time


# criteria: choice must be character in the list
def check_input(a):
    choice_list = ["r", "R", "s", "S", "p", "P"]
    if a in choice_list:
        return a
    else:
        return None


# criteria: let you choose continuously untill it is a valid input
def test(a):
    game = True
    while game == True:
        x = check_input(a)
        if type(x) == str:
            game = False
            return x.upper()
        else:
            a = input("Please choose a valid input. Enter R / P / S : ")


def game_play():
    # get the user input
    user = input("R for rock or P for paper or S for sissor : ")
    user = test(user)  # check if the user input is valid input
    time.sleep(1)

    print("\nYou choose : ", user)

    # generate a random choice for computer
    list = ["R", "P", "S"]
    computer = random.choice(list)
    print("Computer choose : ", computer.upper())

    # win conditions: rock > scissor, scissor > paper, paper > rock
    if user == "R" and computer == "S" or user == "S" and computer == "P" or user == "P" and computer == "R":
        print("Congratulation. You Won !!!")
    elif user == "R" and computer == "R" or user == "S" and computer == "S" or user == "P" and computer == "P":
        print("Its a Draw !!!")
    else:
        print("Sorry. You Lose !!!")


# get play name and choice to play
player = input("Enter your name : ")
play = input("Do you want to start the game? Enter Y/N : ")

# loop to play game continuously if the player chooses yes otherwise end the game
game = True
while game == True:
    if play == "y" or play == "Y":
        game_play()
        time.sleep(3)
        play = input("Do you want to play again? Enter Y/N : ")
        print()
    elif play == 'n' or play == "N":
        print(f"Thank You for playing!!! {player.upper()}.")
        game = False
    else:
        play = input("Please! enter Y / N : ")
