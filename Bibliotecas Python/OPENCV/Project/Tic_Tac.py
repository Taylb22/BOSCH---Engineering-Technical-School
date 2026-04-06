import os
import engine as en
import time

game, map = en.generate_tic_tac()
player = 1

print("Welcome to the Tic-Tac-Toe Game!!!")
while True:
    coordinate = en.show_game(game, player)
    
    if coordinate[0] == None:
        break
    
    r = en.insert_option(game, map, coordinate, player)
    if not r:
        continue
    time.sleep(0.1)
    
    r = en.validate_game(map, player)
    
    if r == True:
        print("VITORIA")
        en.finish(game, map)
        break
    elif r == "velha":
        print("Deu Velha")
        en.finish(game, map)
        break
    
    if player == 1:
        player = 2
    else:
        player = 1