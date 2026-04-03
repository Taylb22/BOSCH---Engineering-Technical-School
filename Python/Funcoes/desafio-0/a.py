import random as rd
from lib import get_data
from typing import List, Tuple, Dict, Any
import copy
import tabulate

def filter(dados : List[Dict[str,str]], colunas_comparacao: str, value: str) -> None:
    dados_copy = []
    for row in dados:
        if row[colunas_comparacao] == value:
            dados_copy.append(row)
    
    return dados_copy

def map(dados : List[Dict[str, Any]], colunas_modificacao : Dict[str, str], value: str) -> None:
    for i in dados:
        for j in colunas_modificacao:
            i[j] = value
        
    return dados



def group(dados : List[Dict[str,str]], colunas_reduzidas : str) -> None:
    grouped = []
                
        



        


dados : List[Dict[str, str]] = get_data('.\gatos.csv', ';')
# filtro = filter(dados, 'Gender', 'male')
# print(tabulate.tabulate(filtro))
# rd.shuffle(dados)

filtroMap = map(dados,'Gender','BUM')
print(tabulate.tabulate(filtroMap))

# filtroGrup = group(dados,'Eye_colour')
# print(tabulate.tabulate(filtroGrup))








