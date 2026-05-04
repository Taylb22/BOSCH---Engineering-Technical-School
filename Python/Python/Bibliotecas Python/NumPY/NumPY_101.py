#Para cálculos de Arrays Multidimensionais
#Cálculos Numéricos

import numpy as np

# lista = [1, 2, 3]

# print(lista)
# print(type(lista))

# listaP = ["Ve", 1]
# array = np.array(listaP)

# print(array)
# print(type(array))

matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(matriz)

mat_numpy = np.array(matriz)
print(mat_numpy)

print(len(matriz))
print(len(matriz[0]))

print(mat_numpy.shape)

print(mat_numpy.ndim)