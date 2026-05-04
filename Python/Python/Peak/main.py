'''
=============================================
Desenvolva uma maneira de encontrar onde 
está o maior valor da matriz.

Exiba o indice de linha e coluna onde o
maior valor se encontra
=============================================
'''

def maior_valor (matriz, linhas, colunas):
    # O(log C) + O(Log L)
    low = 0
    high = colunas - 1
    col_index = 0
    
    while low < high:
        mid = (low + high) // 2
        if matriz[0][mid] < matriz[0][mid + 1]:
            low = mid + 1
        else:
            high = mid
        
        col_index = low
    
    low = 0
    high = linhas - 1
    lin_index = 0
    
    while low < high:
        mid = (low + high) // 2
        if matriz[mid][col_index] < matriz[mid + 1][col_index]:
            low = mid + 1
        else:
            high = mid
        
        lin_index = low
    
    return lin_index, col_index
    
            
from peak_lib import gen_peak

lines = 1000
columns = 1000

montanha = gen_peak(lines,columns,1000)

linha, coluna = maior_valor(montanha, lines, columns)

print(montanha[linha][coluna])