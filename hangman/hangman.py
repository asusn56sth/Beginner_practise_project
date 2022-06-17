# HANGMAN


import string

import random

from words import words


# funtions lets you play the game
def game_play():

    # generate a random word for the user
    word = random.choice(words)

    # converts the word in to sets of letter
    word_letter = {letter.upper() for letter in word}

    # remove the space from the set of letter
    if " " in word_letter:
        word_letter.remove(" ")

    # create a set of all the uppercase alphabet letter
    alphabets = set(string.ascii_letters.upper())
    # variable to stored letter guessed by the player
    guessed_letter = set()
    lives = 8

    # loop only when "lives > 0" and "length of the sets of letter > 0" both are true otherwise ends the loop
    while len(word_letter) > 0 and lives > 0:

        # creates a list of guessed letter, and "_" if not already guessed
        word_list = [letter.upper() if letter.upper(
        ) in guessed_letter else " " if letter == " " else "_" for letter in word]
        # Prints the no. of lives left
        print(f"You have {lives} lives.", "You have used these letters : ", ", ".join(
            guessed_letter))
        # prints the current status of guesses in the word
        print("Current progress : ", " ".join(word_list))

        # get the input from the player
        user_guess = input("Guess a letter : ").upper()
        print()

        # check the input of player guess
        # if player guess fulfill the condition and is not guessed already the add the input to guessed letter
        if user_guess in alphabets - guessed_letter:
            guessed_letter.add(user_guess)
            if user_guess in word_letter:  # if the user guess is in the word then remove the letter for the set of letter
                word_letter.remove(user_guess)
            else:  # if the user guess is is not in the word the print this message and deduct a lives
                print("Sorry! Incorrect Guess.")
                lives -= 1
        elif user_guess in guessed_letter:  # if the user guess is already used, then prints this message
            print("You have already guessed that letter. Try another letter : ")
        else:  # if the user input is not a valid letter then, prints this message
            print("Invalid input! lets try another letter.")

    # check if the user won or lost
    if lives == 0:  # check if the user lost all the lives
        print(f"You lost ! The word is \"{word.upper()}\".")
    else:  # check if the user have guessed all the letter correctly
        print(
            f"Congrulation ! You have guessed the word \"{word.upper()}\" correctly.")


# get the play name and choice to play
user = input("Enter your name : ")
play = input("Do you want to start a Game? Enter Y / N : ")

# this loop lets you play continuously if the player chooses yes otherwise ends the game
game = True
while game == True:
    if play == 'y' or play == 'Y':
        game_play()
        play = input("Do you want to play again ? Enter Y / N : ")
    elif play == 'n' or play == 'N':
        print(f"Thank you for playing ! {user.upper()}.")
        game = False
    else:
        play = input("Please, Enter Y / N : ")
