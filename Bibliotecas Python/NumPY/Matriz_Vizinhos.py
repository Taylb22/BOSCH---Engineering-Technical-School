import numpy as np

n = 4

array = np.random.randint(0, 9, (n, n))
x = np.zeros_like(array)

print(array)
print()

paths = ((0, -1), 
         (-1, 0),
         (0, +1),
         (+1, 0))

for i in range(n * n):
    row = i//(n)
    col = i%(n)

    for cord in paths:
        if ((row + cord[0]) < 0  or (row + cord[0]) > n-1 # Verificação dos limites da linha
            or (col + cord[1])  < 0  or (col + cord[1]) > n-1): # Verificação dos limites da coluna
            continue
        
        x[row, col] += array[row + cord[0], col + cord[1]]

print(x)
print()