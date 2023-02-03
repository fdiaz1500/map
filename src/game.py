#!/usr/bin/env python3

import sys

from player import Player

def play():
    print(' ')
    print('========================')
    print('Escape from Cave Terror!')
    print('========================')
    print(' ')
    player = Player()
    while True:
        action_input = get_player_command()
        if action_input in ['n', 'N']:
            ai_north()
        elif action_input in ['s', 'S']:
            ai_south()
        elif action_input in ['e', 'E']:
            ai_east()
        elif action_input in ['w', 'W']:
            ai_west()
        elif action_input in ['i', 'I']:
            player.print_inventory()
        elif action_input in ['q', 'Q']:
            ai_quit()
        else:
            print('Invalid action!')
        
def get_player_command():
    print(' ')
    print('[ n/N ] North')
    print('[ s/S ] South')
    print('[ e/E ] East')
    print('[ w/W ] West')
    print('[ q/Q ] Quit game')
    print(' ')
    return input('Action: ')

def ai_north():
    print('\nGo North!\n')

def ai_south():
    print('\nGo South!\n')

def ai_east():
    print('\nGo East!\n')

def ai_west():
    print('\nGo West!\n')

def ai_quit():
    print('\nGoodbye..\n')
    sys.exit()

play()