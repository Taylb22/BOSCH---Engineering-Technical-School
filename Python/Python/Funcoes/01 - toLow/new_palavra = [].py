def minuscula (lista):
    new_palavra = [] 
    palavra = "THiago@"
    lista = list(palavra)
    print(palavra)
    for i in lista:
        letra = ord(i)
        if letra >=65 and letra <= 90:
            letra = letra + 32
            letra = chr(letra)
            new_palavra.append(letra)
        else:
            letra = chr(letra)
            new_palavra.append(letra)
    lista = ''.join(new_palavra)
    print(lista)