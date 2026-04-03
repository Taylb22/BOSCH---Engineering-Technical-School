from lib import get_data
import random

# def filter(lista, coluna, valor):

dados = get_data('./desafio-0/gatos.csv', ';')

def filter(lista, coluna1, coluna2, valor1, valor2):
    for i in dados:
        if valor1 in coluna1 and valor2 in coluna2:
            print(i)
            print()

def map(lista, coluna1, coluna2, valor1, valor2):
    for item in lista:
        if coluna1 in item.keys():
            item[coluna1] = valor1
        if coluna2 in item.keys():
            item[coluna2] = valor2
        print(item)

def group(lista, coluna):
    agrupados = []

    for item in lista:
        existe = False

        for dici in agrupados:
            if len(agrupados) != 0:
                if item[coluna] == dici[coluna][0]:
                    for chave in item:
                        if chave != coluna:
                            dici[chave].append(item[chave])
                            existe = True

        if existe == False:
            aux = {}
            for col in item:
                novo_item = {col: [item[col]]}
                aux.update(novo_item)
            agrupados.append(aux)

    return print(agrupados)

random.shuffle(dados)
dados = dados[:5]

filter(dados, 'Breed', 'Gender', ['Maine coon'], ['male', 'female'])