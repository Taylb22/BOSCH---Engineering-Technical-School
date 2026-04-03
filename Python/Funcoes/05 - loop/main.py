import os
import time


#===============================================
#   Crie uma funlçao que move a imagem
#   em X como se fosse uma esteira, portanto
#   o que está na ultima coluna case ande 1
#   para o lado a coluna vai para a primeira
#   coluna 
#===============================================

scene = [
    '    X                         X               X   ',
    '    X                        XX  X           XX   ',
    '   XX       X               XXXX XX          XXX  ',
    '   XXX      XX       X      XXXXXXXX         XXXX ',
    '  XXXXX    XXXX     XX     XXXXXXXXX        XXXXX ',
    ' XXXXXX   XXXXX    XXX    XXXXXXXXXXX       XXXXXX',
    ' XXXXXX  XXXXXXX   XXX    XXXXXXXXXXX      XXXXXXX',
    ' XXXXXXX XXXXXXX  XXXXX   XXXXXXXXXXXX     XXXXXXX',
    ' XXXXXXX XXXXXXXXXXXXXX  XXXXXXXXXXXXXX   XXXXXXXX',
]


# def moveX(
#         scene, step=-1
# ):
#     rows = len(scene)
#     columns = len(scene[0])
    
#     for i in range(rows):
#         linha = list(scene[i])
#         ult = linha[-1]
#         for j in range(columns - 1, -1, -1):
#             if not(j == 0):
#                 linha[j] = linha[j + step]
#             else:
#                 linha[0] = ult
#         scene[i] = "".join(linha)
    
def moveX(step):
    scene_copy = scene.copy()
    
    for col in range(len(scene[0])):
        for lin in range(len(scene)):
            aux = list(scene_copy[lin])
            aux[(col + step) % (len(scene[0]))] = scene[lin][col]
            scene_copy[lin] = ''.join(aux)
    
    return scene_copy

for i in range(100000):
    scene = moveX(
        1
    )

    for i in scene:
        print(i)
        
    time.sleep(0.01)
    os.system('cls')
