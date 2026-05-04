import re

def cifra_cesar(texto:str, deslocamento:int):
    lista_novo_texto = []
    
    for char in texto:
        novo_char =  chr(((ord(char) + deslocamento - ord('a')) % 26) + ord('a'))
        lista_novo_texto.append(novo_char)
    
    texto = ''.join(lista_novo_texto)
    return texto

def validar_email(email:str):
    regex_pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    if re.search(regex_pattern, email) != None:
        return True
        
    return False

nome = input('Digite o nome a ser cadastrado: ')

while True:
    email= input('Digite o email a ser cadastrado: ')
    retorno = validar_email(email)
    
    if retorno:
        break
    
    print("O email não foi reconhecido, verifique seu email.")
    
senha = input('Digite a senha a ser criada: ')

senha = cifra_cesar(senha, 1)

with open('./usuarios.txt', 'a') as df:
    df.writelines(f'{nome};{email};{senha}\n')

with open('./usuarios.txt', 'r') as df:
    for line in df.readlines():
        lista_user = line.split(';')
        print(f'{lista_user[1]} | {lista_user[2]}')