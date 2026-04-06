import cv2
import numpy as np
import math as m

mX = None
mY = None

#FINALIZAÇÂO
def finish(game, map):
    cv2.imshow('Tic-Tac-Toe', game)
    
    # cv2.line()
    
    cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()

#======================================================================
#VALIDAÇÕES
def validate_insertion(map, coordinates, player):
    Qs = {
        (175, 175) : (0, 0), (350, 175) : (0, 1), (525, 175) : (0, 2),
        (175, 350) : (1, 0), (350, 350) : (1, 1), (525, 350) : (1, 2),
        (175, 525) : (2, 0), (350, 525) : (2, 1), (525, 525) : (2, 2),
    }
    
    i = Qs[coordinates]
    if map[i] != 0:
        return False
    map[i] = player
    return True

def validate_game(map, player):
    mask = (map == np.full(3, player))
    
    if (np.any(np.all(mask, axis=1)) or 
        np.any(np.all(mask, axis=0)) or
        np.any(np.all(mask.diagonal())) or
        np.any(np.all(np.fliplr(mask).diagonal()))):
        return True
    
    mask = (map != 0)
    
    if np.all(mask):
        return "velha"
    
    return False

#======================================================================
#Geração de Imagens
def gen_circle(game, center):
    cv2.circle(game, center, 50, (255, 255, 255), 3)

def gen_X(game, center):
    cv2.line(game, (center[0] - 50, center[1] - 50), (center[0] + 50, center[1] + 50), (255, 255, 255), 3)
    cv2.line(game, (center[0] - 50, center[1] + 50), (center[0] + 50, center[1] - 50), (255, 255, 255), 3)

#======================================================================
#Inserção de Imagens
def insert_option(game, map, coordinates, player):
    limits = (
        175,
        350,
        525,
    )
    
    q = [0, 0]
    for limit in limits:
        if coordinates[0] <= limit:
            q[0] = limit
            break
    
    for limit in limits:
        if coordinates[1] <= limit:
            q[1] = limit
            break
    
    if not validate_insertion(map, tuple(q), player):
        return False
    
    center = [m.floor(q[0] - (175 / 2)), m.floor(q[1] - (175 / 2))]

    match player:
        case 1:
            gen_X(game, center)
        case 2:
            gen_circle(game, center)
    return True
            

#======================================================================
#Exibição gráfica do jogo e rastreio de eventos do Mouse
def show_game(game, player):
    text = "Player " + str(player)
    # cv2.putText(game, text, (180, 520), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 125), 2)
    cv2.imshow('Tic-Tac-Toe', game)
    cv2.setMouseCallback("Tic-Tac-Toe", mouse_click)
    while True:
        if cv2.waitKey(1) & 0xFF == 27 or (mX != None and mY != None):
            break
    return (mX, mY)

def mouse_click(event, x, y, flags, param):
    global mX, mY
    if event == cv2.EVENT_LBUTTONDOWN:
        mX, mY = x, y
    else:
        mX, mY = None, None

#======================================================================
#Criação da imagem e mapa do jogo
def generate_tic_tac():
    img = np.zeros((525, 525, 3), np.uint8)
    
    lines = [
        ((175, 0), (175, 525)),
        ((350, 0), (350, 525)),
        ((0, 175), (525, 175)),
        ((0, 350), (525, 350))
    ]
    
    for line in lines:
        cv2.line(img, line[0], line[1], (255, 255, 255), 4)
    
    map = np.zeros((3, 3))
    
    return img, map