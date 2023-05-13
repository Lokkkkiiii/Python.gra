import os
import msvcrt
import time
import random

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_game_board(player_position, objects_positions, map):
    clear_console()
    for row in range(len(map)):
        for col in range(len(map[row])):
            if row == len(map) - 1 and col == player_position:
                print('O', end='')
            elif (row, col) in objects_positions:
                print('X', end='')
            else:
                print(' ', end='')
        print()

def update_player_position(player_row, player_position):
    return (player_row, player_position)

def update_objects_positions(objects_positions):
    return [(row + 1, col) for row, col in objects_positions]

def create_new_object():
    return (0, random.randint(0, 7))

def check_collision(player_row, player_position, objects_positions):
    for pos in objects_positions:
        if  pos[1] == player_position and pos[0] == player_row:
            return True
    return False

def game():
    player_position = 0
    objects_positions = [create_new_object()]
    map = [['#']*8 for _ in range(8)]
    player_row = len(map) - 2
    while True:
        print_game_board(player_position,objects_positions, map)
        time.sleep(0.5)
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'a':
                player_position = max(0, player_position - 1)
            elif key == b'd':
                player_position = min(len(map[0]) - 1, player_position + 1)
        if random.random() < 1:
            objects_positions.append(create_new_object())
        objects_positions = [pos for pos in objects_positions if pos[0] < len(map) - 1]
        objects_positions = update_objects_positions(objects_positions)
        if check_collision(player_row, player_position, objects_positions):
            print_game_board(player_position, objects_positions, map)
            print("Game Over!")
            time.sleep(2)
            break
        player_row, player_position = update_player_position(player_row, player_position)

game()
