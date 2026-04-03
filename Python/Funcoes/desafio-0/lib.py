from typing import List, Dict

def get_data(path : str, split : str) -> List[Dict[str,str]]:
    with open(path, 'r') as file:
        cabecalho : List[str] = file.readline().split(split)
        cabecalho[0] = 'Breed'
        dados : List[Dict[str,str]] = []
        for linha in file.readlines():
            linha = linha.split(split)
            dados_linha : Dict[str,str] = {}
            for i in range(len(linha)):
                linha[i] = linha[i].strip()
                dados_linha[cabecalho[i].strip()] = linha[i]
            dados.append(dados_linha)
    return dados