import random as rd
import typing
import copy

def gen_pyramid(size: int) -> list[list[int]]:
    pyramid = [[rd.randint(1, 10) for j in range(i)] for i in range(1, size + 1)]
    return pyramid

memo = {}
def index_best(pyramid : list[list[int]], row : int, index : int):
    key = (row, index)
    
    if key in memo:
        result_r, result_s = memo[key]
        return result_r, result_s
    
    value = pyramid[row][index]
    
    if (row  + 1) > len(pyramid) - 1:
        memo[key] = ([value], value)
        return [value], value
    
    l_route, l_sum = index_best(pyramid, row + 1, index)
    r_route, r_sum = index_best(pyramid, row + 1, index + 1)
    
    if l_sum > r_sum:
        b_route = [value] + l_route
        b_sum = value + l_sum
    else:
        b_route = [value] + r_route
        b_sum = value + r_sum
        
    memo[key] = (b_route, b_sum)
    return b_route, b_sum
    
def best_route(pyramid: list[list[int]]):
    memo.clear()
    return index_best(pyramid, row=0, index=0)

size = 100
pyramid = gen_pyramid(size)

for i in range(len(pyramid)):
    print(' '*(size-i), end='')
    for j in range(len(pyramid[i])):
        print(pyramid[i][j], " ", end='')
    print()
    
r, s = best_route(pyramid)

print()
print(f'Route: {r}\nSum: {s}')