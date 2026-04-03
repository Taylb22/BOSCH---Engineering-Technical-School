import numpy as np

n = 3

array = np.zeros((n, n))

print(array)
print()

for i in range(n):
    array[i,i] = 1
    array[i,n-1-i] += 2

print(array)