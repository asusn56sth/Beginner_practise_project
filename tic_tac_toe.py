# TIC TAC TOE


# function to show rules at the start of the game
def game_rule():
    # rules to play the game are displayed at the start of the game
    board = [i for i in range(1, 10)]
    instruction = "HOW TO PLAY THE GAME!"
    rules = """
    1. The TIC TAC TOE board is a simple and easily drawn 3 X 3 grid.
    2. Players take turns putting an \"X\" or \"O\"in the middle of the grid.
    3. There are three possible winning patterns: Vertical, Horizantal, Diagonal.
    4. Player who enters the three spot first wins the game.
    5. Enter the number from 1 to 9 to choose a spot.
    """
    print(instruction.center(80, "-"))

    print("", board[0], "|", board[1], "|", board[2])
    print("---|---|---")
    print("", board[3], "|", board[4], "|", board[5])
    print("---|---|---")
    print("", board[6], "|", board[7], "|", board[8])

    print(rules.ljust(80, " "))


# function to display the board
# display the board and update the changes in the board
def display_board():
    global board

    print("\n", board[1], "|", board[2], "|", board[3])
    print("---|---|---")
    print("", board[4], "|", board[5], "|", board[6])
    print("---|---|---")
    print("", board[7], "|", board[8], "|", board[9], "\n")


# function to control the player 1
def player_1():
    global player1_name
    input1 = int(input(player1_name + " turn : "))
    while True:
        if input1 in range(1, 10):
            if input1 not in used_number:
                return input1
            else:
                input1 = int(
                    input("That spot is already taken. Please choose another spot : "))
        else:
            input1 = int(input("Please enter a number between 1 to 9 : "))


# function to control the player 2
def player_2():
    global player2_name
    input2 = int(input(player2_name + " turn : "))
    while True:
        if input2 in range(1, 10):
            if input2 not in used_number:
                return input2
            else:
                input2 = int(
                    input("That spot is already taken. Please choose another spot : "))
        else:
            input2 = int(input("Please enter a number between 1 to 9 : "))

# function to check the winner


def check_win():
    global player1_number
    global player2_number
    global win_condition

    if len(player1_number) > 2:
        list1 = [i for i in win_condition if all(
            x in player1_number for x in i)]
        for i in list1:
            if i in win_condition:
                return 1

    if len(player2_number) > 2:
        list2 = [i for i in win_condition if all(
            x in player2_number for x in i)]
        for i in list2:
            if i in win_condition:
                return 2


game_rule()
print("Welcome to the TIC TAC TOE game.\n")
player1_name = input("Player1 name : ")
player2_name = input("Player2 name : ")

board = {
    1: " ", 2: " ", 3: " ",
    4: " ", 5: " ", 6: " ",
    7: " ", 8: " ", 9: " ",
}

used_number = []
player1_number = []
player2_number = []
win_condition = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [
    1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

for i in range(1, 9):
    display_board()
    if i % 2 != 0:
        x = player_1()
        player1_number.append(x)
        used_number.append(x)
        board[x] = "X"

    else:
        x = player_2()
        player2_number.append(x)
        used_number.append(x)
        board[x] = "O"

    c = check_win()
    if c == 1:
        display_board()
        print(f"Congratulation! {player1_name} You win>")
        break
    if c == 2:
        display_board()
        print(f"Congratulation! {player2_name} You win>")
        break

    if i == 8:
        display_board()
        print("Its a Draw.")
        break
