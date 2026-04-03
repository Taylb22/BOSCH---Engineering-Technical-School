from lib import init, get_height, get_width

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


def func(obj, objs, t):
    return obj



e = [

    {'label' : 'bola', 'pos_xy' : (100,100), 'velocities_xy' : (0,0), 'color' : 'green', 'ray' : 30, 'behavior' : func},
]

init(entities=e, fps=60)