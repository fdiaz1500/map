#!/usr/bin/env python3

import sys
import cgi
import cgitb


from player import Player

def play():
    print(' ')
    print('========================')
    print('Escape from Cave Terror!')
    print('========================')
    print(' ')

    # Setup envrionment
    player  = Player()
    form    = cgi.FieldStorage()
    user    = form.getfirst('user', '').upper()  # This is thread safe

    # Main game loop
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
            print(' ')
            player.print_inventory()
        elif action_input in ['q', 'Q']:
            ai_quit()
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


if __name__ == '__main__':
    play()