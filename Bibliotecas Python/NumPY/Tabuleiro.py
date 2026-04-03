import numpy as np
import typing

def table_estatistics(n: int) -> any:
    array = np.random.randint(0, 101, (n, n))

    mean = array.mean()
    print(f"\nMean: {mean}\n")
    maxim = array.max()
    print(f"Maximun: {maxim}\n")
    minim = array.min()
    print(f"Minumim: {minim}\n")

    result = np.zeros_like(array)

    minus_mean = (array < mean)
    bigger_mean = (array > mean)
    equals_max = (array == maxim)
    equals_min = (array == minim)

    result[minus_mean] = -1
    result[equals_min] = -9
    result[bigger_mean] = 1
    result[equals_max] = 9

    return array, result

values, table = table_estatistics(4)

print(values)
print()
print(table)
print()