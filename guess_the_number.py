# GUESS THE NUMBER


import random


def check_digit(A):
    # criteria1: number must be digit otherwise return none
    if A.isdigit() == True:
        return int(A)
    else:
        return None


def test(a):
    # criteria2: number must be positive integer
    # loops end only if user input is a positive number
    bound = True
    while bound == True:
        x = check_digit(a)
        if type(x) == int:
            bound = False
            return x
        else:
            a = input("Please! enter a positive integer value : ")


def game_play():
    # get the upper bound limt from the user and check the criteria2
    upper_bound = input("Please enter a upper bound : ")
    upper_bound = test(upper_bound)

    # generate a ramdom number to be guessed by the user
    secret = random.randint(1, upper_bound)

    # get a number from the player and check the criteria
    print("Guess a number between 1 and " + str(upper_bound) + " : ")
    user_guess = input()
    user_guess = test(user_guess)

    # checks the player input number is correct and counts the user attempts
    attempt = 1
    flag = True
    while flag == True:

        if user_guess < secret:
            user_guess = int(input("HINT: Enter a highr value "))
            attempt += 1
        elif user_guess > secret:
            user_guess = int(input("HINT: Enter a lower value "))
            attempt += 1
        elif user_guess == secret:
            flag = False

    # print the no. of attempts and print results
    print("CONGRATULATION! You have guess the number in ", attempt, " attempts.")


# Get player name and choice to play
player_name = input("Enter your Name : ")
play = input("Do you want to start the game? Enter Y/N : ")

# loop to play game continuously if chooses yes otherwise end the game
game = True
while game == True:
    if play == "y" or play == "Y":
        game_play()
        play = input("Do you want to play again? Enter Y/N : ")
    elif play == "n" or play == "N":
        print("Thank you! for playing. " + player_name.upper())
        game = False
    else:
        play = input("Please! Enter Y / N :")
