import numpy as np

notas = np.random.randint(0, 10, (100, 6))
print(notas.size)

copia = np.copy(notas)
copia = copia.reshape((50, 12))
# print(copia[20:30, 2:4])

mask = (copia < 5)
copia[mask] = 5
print(copia)
print()

means = np.round(np.mean(copia, axis=1), decimals=2)
means = means.reshape(-1, 1)
copia = np.concatenate((copia, means), axis=1)
print()

print(copia)