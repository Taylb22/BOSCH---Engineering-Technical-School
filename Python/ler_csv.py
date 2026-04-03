# def ler_csv (arquivo:str, sep:str):
#     df = {}
    
#     with open(arquivo, 'r') as arq:    
#         for word in arq.readline().split(sep):
#             df[word] = []
        
#         for line in arq.readlines():
#             split_line = line.split(sep)
#             item = 0
#             for column in df:
#                 df[column].append(split_line[item]) 
#                 item += 1

#         arq.close()        
#     return df

#def filtrar(coluna:str, ):

def funcao(callable):
    lista = [1,2,3,4,5,6]
    lista_retorno = []
    
    for e in lista:
        if callable(e):
            lista_retorno.append(e)
    return lista_retorno
    
a = funcao(lambda x : x < 2)
print(a)

# arquivo = "./cat_breeds.csv"
# df = ler_csv(arquivo, ";")

# print(df["Age_in_years"])