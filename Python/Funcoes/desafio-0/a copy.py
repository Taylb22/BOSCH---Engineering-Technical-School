import random as rd
from lib import get_data
from typing import List, Tuple, Dict, Any
import copy
import tabulate

def filter(dados : List[Dict[str,str]], colunas_comparacao: str, value: str) -> None:
    dados_copy = copy.deepcopy(dados)
    
    for row in dados:
        if row[colunas_comparacao] == value:
            dados_copy.append(row)
    
    return dados_copy
            

def map(dados : List[Dict[str, Any]], colunas_modificacao : Dict[str, str]) -> None:
    pass
def group(dados : List[Dict[str,str]], colunas_reduzidas : List[str]) -> None:
    pass


dados : List[Dict[str, str]] = get_data('.\gatos.csv', ';')
filter(dados, 'Age_in_months', '3')
rd.shuffle(dados)
