import os
import msvcrt
import time
import random

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_game_board(player_x, player_y, falling_objects, mapa):
    clear_console()
    for row in range(len(mapa)):
        for col in range(len(mapa[row])):
            if row == len(mapa) - 1 and col == player_x:
                print('O', end='')
            elif (row, col) in falling_objects:
                print('X', end='')
            else:
                print(mapa[row][col], end='')
        print()

def update_object_position(player_y, player_x):
    return (player_y + 1, player_x)

def update_falling_objects(falling_objects):
    return [(row + 1, col) for row, col in falling_objects]

def create_new_object():
    return (0, random.randint(0, 7))

def game():
    player_x = 0
    falling_objects = [create_new_object()]
    mapa = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    player_y = len(mapa) - 2
    while True:
        print_game_board(player_x, player_y, falling_objects, mapa)
        time.sleep(0.5)
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'a':
                if(player_x<8):
                    player_x = max(0, player_x - 1)
            elif key == b'd':
                if(player_y<8):
                    player_x = min(len(mapa[0]) - 1, player_x + 1)
        if random.random() < 0.2:
            falling_objects.append(create_new_object())
        falling_objects = [pos for pos in falling_objects if pos[0] < len(mapa) - 1]
        falling_objects = update_falling_objects(falling_objects)
        if (player_x, player_y) in falling_objects:

            print("Game Over!")
            break
        player_y, player_x = update_object_position(player_y, player_x)

game()
