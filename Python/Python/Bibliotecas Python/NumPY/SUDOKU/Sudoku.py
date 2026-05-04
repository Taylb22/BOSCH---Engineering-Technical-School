import numpy as np
import typing

def read_game(path : str) -> np.ndarray:
    game = np.array([])
    with open(path, "r") as txt:
        for line in txt.readlines():
            for char in line:
                if char.isnumeric():
                    game = np.append(game, int(char))
    return game.reshape(9, 9)
 
def validate_game(game : np.ndarray) -> bool:
    for line in game:
        if not(np.array_equal(np.sort(line), np.arange(1, 10))):
            return False
   
    for col in game.T:
        if not(np.array_equal(np.sort(col), np.arange(1, 10))):
            return False
   
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            aux = game[i:i + 3, j:j + 3].flatten()
           
            if not(np.array_equal(np.sort(aux), np.arange(1, 10))):
                return False
    return True
 
game : np.ndarray = read_game("S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Bibliotecas Python/NumPY/SUDOKU/Sudoku_Game2.txt")
print(game)
print()
print(np.sort(game[0]))
print(np.arange(1, 10))
print()
print(validate_game(game))