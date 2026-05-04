import random as rd
from lib import init, get_height, get_width
import math

# A função recebe o objeto que esta sendo simulado, os outros objetos presentes na tela, e o tempo desde a última movimentação.
# Cada objeto tem a seguinte estrutura:

# =========================================
# ||                                     ||
# ||    obj : {                          ||
# ||              x             : _      ||
# ||              y             : _      ||
# ||              velocity_x    : _      ||
# ||              velocity_y    : _      ||
# ||              ray           : _      ||
# ||    }                                ||
# ||                                     ||
# =========================================


# Implemente uma função chamada 'dvd()', que tem o comportamento igual ao de televisões quando ficam ociosas
# Implemente uma função chamada 'gravidade()' que aplica gravidade aos objetos | aceleração = 980 (pixels/s², 100px -> 1m, 980px -> 9.8m)
# Se divirta e fique livre para implementar o que quiser dentro de sua simulação :)


def gravidade_terra(obj, objs, t):
    a = 980

    obj['velocity_y'] = obj['velocity_y'] + a * t
    obj['y'] = obj['y'] + obj['velocity_y'] * t

gravidades = {
    
}

def gravidade_lua(obj, objs, t):
    a = 168
    y = obj['y']
    x = obj['x']
    Vy = obj['velocity_y']
    Vx = obj['velocity_x']
    ray = obj['ray']

    #Colisões de paredes
    if y + ray > get_height() or y - ray < 0:
        Vy = (-0.85) * Vy
        
    if x + ray > get_width() or x - ray < 0:
        Vx = (-0.85) * Vx
    
    #Colisões entre os Discos
    for disco in objs:
        distY = y - disco['y']
        distX = x - disco['x']
        distance = math.sqrt(distX**2 + distY**2)
        if distance < ray + disco['ray']:
            Vy = (-1) * Vy
            Vx = (-1) * Vx
            disco['velocity_y'] = (-1) * disco['velocity_y']
            disco['velocity_x'] = (-1) * disco['velocity_x']
            
            
    if Vy < 250:
        Vy = Vy + a * t
    else:
        Vy = 250
    y = y + Vy * t
    
    if Vx < 250 and Vx > -250:
        Vx = Vx + Vx * t
    elif Vx > 250:
        Vx = 250
    elif Vx < -250:
        Vx = - 250
        
    x = x + Vx * t

    obj['y'] = y
    obj['velocity_y'] = Vy
    
    obj['x'] = x
    obj['velocity_x'] = Vx
e = [
    {
        'label' : 'bola', 
        'pos_xy' : (100,100), 
        'velocities_xy' : (75,0), 
        'color' : 'green', 
        'ray' : 30, 
        'behavior' : gravidade_lua
    },
    
    {
        'label' : 'bola2', 
        'pos_xy' : (800,100), 
        'velocities_xy' : (-75,0), 
        'color' : 'yellow', 
        'ray' : 30, 
        'behavior' : gravidade_lua
    }
]

init(entities=e, fps=100)