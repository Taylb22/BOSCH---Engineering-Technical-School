import numpy as np

#==================================================================================================
# Desafio 1
# my_array = np.arange(0, 110, 10)
# print(my_array)

#==================================================================================================
# Desafio 2
# array = np.zeros((2, 2))
# print(array)

#==================================================================================================
# Desafio 3
# array = np.ones((5, 2))
# print(array)

#==================================================================================================
# Desafio 4
# array =  np.full((5,2), 6)
# print(array)

#==================================================================================================
# Desafio 5
# array = np.full((10, 10), True)
# print(array)

#==================================================================================================
# Desafio 6
# print(np.linspace(1, 6, 9))
# print(np.linspace(2, 3, 5))

#==================================================================================================
# Desafio 7
# print(np.random.rand(2, 2))
# print(np.random.randint(0, 10, (2, 10)))

#==================================================================================================
# Desafio 8 #Estatística
# array = np.random.randint(0, 10, (2, 2))
# print(array)
# print()
# print(f"MAX = {array.max()}")
# print(f"MIN = {array.min()}")
# print(f"Index_Max = {array.argmax()}")
# print(f"Index_Min = {array.argmin()}")
# print(f"Mean = {array.mean()}")
# print(f"STD_Deviation = {array.std()}")
# print(f"Variation = {array.var()}")
# print(f"Median = {np.median(array)}")

#==================================================================================================
# Desafio 9 #Indexação
# array = np.random.randint(0, 100, 5)
# print(array)
# print()
# print(array[0])
# print()
# print(array[:2])
# print()
# print(array[:4:2])

#==================================================================================================
# Desafio 10
# array = np.random.randint(0, 10, (4, 4))
# print(array)
# print()
# print(array[2, 2])
# print()
# print(array[:2,:2])
# print()
# print(array[array > 3])

#==================================================================================================
# Desafio 11
# array = np.random.randint(0, 10, 9).reshape((3, 3))
# print(array)
# print()
# filtrado = (array%2!=0) #Máscara
# print(filtrado)
# array[filtrado] = 0 #Comparação com a Máscara
# print()
# print(array)

#==================================================================================================
# Desafio 12