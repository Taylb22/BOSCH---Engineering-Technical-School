import numpy as np

array = np.random.randint(0, 10, 6).reshape((3, 2))
print(array)
print()

array[:1,:] = np.add(array[:1,:], 5)
print("Soma da primeira linha: ")
print(array)
print()

array[1:2,:] = np.multiply(array[1:2,:], 3)
print("Multiplicação da segunda linha: ")
print(array)
print()

array[:, 1:2] = np.divide(array[:, 1:2], 2)
print("Divisão da segunda coluna: ")
print(array)
print()