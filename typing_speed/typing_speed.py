# This is a python file to test your typing speed.
# First of all, pip install windows-curses.
# Change the file location of 'text.txt' in main.py file line 42.
# Run the code.
# Enjoy!!!

import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):

    # clears the screen
    stdscr.clear()

    stdscr.addstr('TEST YOUR TYPING SPEED!')
    stdscr.addstr('\nPress any key to start!')

    # refreshes the screen
    stdscr.refresh()

    # wait for the user to type something
    key = stdscr.getkey()


def display_text(stdscr, target, current, wpm=0, cpm=0, time_els=0):
    '''
    display the text on the standard screen
    '''
    stdscr.addstr(target)
    stdscr.addstr(2, 0, f'WPM : {wpm}')
    stdscr.addstr(2, 12, f'CPM : {cpm}')
    stdscr.addstr(2, 24, f'TIME ELAPSED : {time_els}')

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)


def text_file():
    '''
    randomly select a line from the text.txt file.
    '''
    with open('typing_speed\\text.txt', 'r') as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def wpm_test(stdscr):
    '''
    test the speed of the typing and counts the mistakes,
    '''

    target_text = text_file()
    current_text = []
    wpm = 0
    cpm = 0
    mistake = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:

        time_elapsed = max(time.time() - start_time, 1)
        cpm = round(len(current_text)/(time_elapsed/60))
        wpm = round((len(current_text)/(time_elapsed/60))/5)
        time_elapse = round(time_elapsed)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm, cpm, time_elapse)
        stdscr.refresh()

        if ''.join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        # if the user press esc key, program exits.
        if ord(key) == 27:
            break

        # if the user press backscape key, then the last pressed word is deleted.
        if key in ('\b', 'KEY_BACKSPACE', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
                mistake += 1
        # if user type more words than the actual text then noting is printed in screen.
        elif len(current_text) < len(target_text):
            current_text.append(key)

    accuracy = round(((len(target_text)-mistake)/len(target_text))*100)
    stdscr.addstr(
        4, 0, f"COMPLETED!!! \nYour typing speed was {wpm} WPM ({cpm} CPM). Your accuracy is {accuracy}%.", curses.color_pair(4))


def main(stdscr):
    '''
    takes over the stadard terminal screen and gives you a screen over top of it that allows you to write stuff to the screen
    '''
    # adding color pair to the string in foreground and background along with the id eg. 1,2,3
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)

    # assigning the color pair to the string using id no.
    # stdscr.addstr('Hello world!', curses.color_pair(1))
    # assigning the position of row and column, where the text should start in the terminal
    # stdscr.addstr(1, 0, 'Hello world!')

    start_screen(stdscr)
    # loops over continuously until the player hits esc key
    while True:
        wpm_test(stdscr)
        stdscr.addstr(
            6, 0, f"Press any key to try again... or press Esc to exit!", curses.color_pair(5))
        key = stdscr.getkey()
        if ord(key) == 27:
            break


# it lest you run the code in the terminal.
wrapper(main)
