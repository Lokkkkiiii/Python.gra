import os
import msvcrt
import time
import random

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def mapa(player_x, meteory, map):
    clear_console()
    for row in range(len(map)):
        for col in range(len(map[row])):
            if row == len(map) - 1 and col == player_x:
                print('O', end='')
            elif (row, col) in meteory:
                print('X', end='')
            else:
                print(' ', end='')
        print()

def update_player(player_y, player_x):
    return (player_y, player_x)

def update_meteory(meteory):
    return [(row + 1, col) for row, col in meteory]

def create_meteory():
    return (0, random.randint(0, 9))

def check_collision(player_y, player_x, meteory):
    for pos in meteory:
        if  pos[1] == player_x and pos[0] == player_y+1:
            return True
    return False

def game():
    player_x = 0
    meteory = [create_meteory()]
    map = [[' ']*10 for _ in range(10)]
    player_y = len(map) - 2
    while True:
        mapa(player_x,meteory, map)
        time.sleep(0.4)
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'a':
                player_x = max(0, player_x - 1)
            elif key == b'd':
                player_x = min(len(map[0]) - 1, player_x + 1)
        if random.random() < 1:
            meteory.append(create_meteory())
        meteory = [pos for pos in meteory if pos[0] < len(map) - 1]
        meteory = update_meteory(meteory)
        if check_collision(player_y, player_x, meteory):
            mapa(player_x, meteory, map)
            print("Przegrałes")
            break
        player_y, player_x = update_player(player_y, player_x)

game()
