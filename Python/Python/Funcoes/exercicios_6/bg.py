from lib import *

def count_neighbour(e, emap) -> int:
    coordinates = [
        (-1, -1), (-1, 0), (-1, 1),
        (0,  -1),          (0,  1),
        (1,  -1), (1,  0), (1,  1)
    ]
    
    n = 0
    
    lines = len(emap)
    columns = len(emap[0])
    
    for line in range(lines - 1):
        for column in range(columns - 1):
            if emap[line][column] != None and emap[line][column]['label'] == e['label']:
                for x, y in coordinates:
                    if emap[line + x][column + y] != None:
                        n += 1
                break
    return n
    

def new_neighbour(e, emap):
    n = count_neighbour(e, emap)
    if n >= 1:
        print('oxes')

def square(bg_map: list, A: tuple, B:tuple, filled = True, color = (100, 100, 100)) -> list:
    if A[0] > B[0]:
        stepY = -1
    else:
        stepY = 1
        
    if A[1] > B[1]:
        stepX = -1
    else:
        stepX = 1
    
    if filled:
        for i in range(A[0], B[0] + stepY, stepY):
            for j in range(A[1], B[1] + stepX, stepX):
                bg_map[i][j] = color
    else:
        for i in range(A[0], B[0] + stepY, stepY):
            bg_map[i][A[1]] = color
            bg_map[i][B[1]] = color
            
            for j in range(A[1], B[1] + stepX, stepX):
                bg_map[A[1]][j] = color
                bg_map[B[1]][j] = color

height = 10
width = 10
pixel_size = 50

background_map = get_map(width, height, pixel_size)
e_map = get_map(width, height, pixel_size)

e_me = {
    'label' : 'Find_Neighbour1',
    'z'     : 1,
    'color' : (255, 0, 0),
    'func'  :  new_neighbour
}

e_test = {
    'label' : 'Find_Neighbour2',
    'z'     : 1,
    'color' : (255, 0, 0),
    'func'  :  new_neighbour
}

e_test2 = {
    'label' : 'Find_Neighbour3',
    'z'     : 1,
    'color' : (255, 0, 0),
    'func'  :  new_neighbour
}

e_map[4][4] = e_me
e_map[5][5] = e_test
e_map[4][5] = e_test2

#square(background_map, (9, 9), (0, 0), False, (255, 255, 255))
start(e_map=e_map, bg_map=background_map, bg=(255, 255, 255), actions_per_second=1, show_len=True)