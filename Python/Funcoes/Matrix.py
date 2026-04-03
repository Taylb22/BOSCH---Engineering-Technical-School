import random as rd
import tabulate
import copy

def order_index():
    pass

def max_index(matrix: list) -> list:
    book = copy.deepcopy(matrix)
    
    for paper in book:
        for line in paper:
            bigger = max(line)
            bigger_index = line.index(bigger)
            line.clear()
            line.append(bigger_index)
    return book

matrix = [[[rd.randint(1, 10) for i in range(3)] for j in range(5)] for z in range(5)]
index_matrix = max_index(matrix)

print(tabulate.tabulate(matrix))
print(tabulate.tabulate(index_matrix))