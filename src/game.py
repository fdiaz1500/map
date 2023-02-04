#!/usr/bin/env python3

import sys
# import cgi
# import cgitb
# cgitb.enable()
import tkinter as tk

from player import Player

def play():
    print(' ')
    print('========================')
    print('    Move and Pivot!')
    print('========================')
    print(' ')

    # Create player
    player  = Player()

    # Main game loop
    while True:
        action_input = get_player_command()
        if action_input in ['n', 'N']:
            move_north()
        elif action_input in ['s', 'S']:
            move_south()
        elif action_input in ['e', 'E']:
            move_east()
        elif action_input in ['w', 'W']:
            move_west()
        elif action_input in ['i', 'I']:
            print(' ')
            player.print_inventory()
        elif action_input in ['q', 'Q']:
            quit_app()
        else:
            print('Invalid action!')
        
def get_player_command():
    print(' ')
    print('[ n/N ] move north')
    print('[ s/S ] move south')
    print('[ e/E ] move east')
    print('[ w/W ] move west')
    print(' ')
    print('[ i/I ] show inventory')
    print('[ q/Q ] quit game')
    print(' ')
    return input('Action: ')

def move_north():
    print('\nGo North!\n')

def move_south():
    print('\nGo South!\n')

def move_east():
    print('\nGo East!\n')

def move_west():
    print('\nGo West!\n')

def quit_app():
    print('\nGoodbye..\n')
    sys.exit()

def gui():
    root = tk.Tk()
    root.title('Move and Pivot - A text adventure game')

    label = tk.Label(root, text='')
    label.pack()

    start_button = tk.Button(root, text='Start game', command=play)
    start_button.pack()

    root.mainloop()

if __name__ == '__main__':

    try:
        # Check if argument passed in
        args = sys.argv[1]
    except Exception as e:
        # print(e)
        args = None

    if args:
        gui()
    else:
        play()