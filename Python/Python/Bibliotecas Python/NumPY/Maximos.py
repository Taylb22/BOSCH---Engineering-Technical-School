import numpy as np

n = 10
array = np.random.randint(0, 20, (n, n))
mask = np.zeros_like(array)

print(array)
print()

paths = (
    (-1, 0), # cima
    (+1, 0), # baixo
    (0, -1), # esquerda
    (0, +1)  # direita
)

for i in range(n * n):
    row = i//n
    col = i%n
    is_peak = (1 << 0)
    for cord in paths:
        if ((row + cord[0]) < 0 or (row + cord[0]) > n-1
            or (col + cord[1]) < 0 or (col + cord[1]) > n-1):
            continue
        
        if array[row + cord[0], col + cord[1]] > array[row, col]:
            is_peak = (is_peak ^ 1 << 0)
            break
    if (is_peak << 0) == 1:
        mask[row, col] = 1

print(mask)
print()