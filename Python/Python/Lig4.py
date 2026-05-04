from colorama import Fore, init, Style

def colocar_disco(coluna: int, matriz, player):
    for j in range(5, -1, -1):
        if matriz[j][coluna] == " ":
            matriz[j][coluna] = player
            return matriz, True
    return matriz, False #retorna falso caso a coluna esteja conpletamente preenchida

def exibir_matriz(matriz):
    print()
    for i in range(0, 6):
        for j in range(0, 10):
            if matriz[i][j] == 1:
                print("|" + Fore.YELLOW + " O " + Style.RESET_ALL + "|", end="")
            elif matriz[i][j] == 2: 
                print("|" + Fore.BLUE + " O " + Style.RESET_ALL + "|", end="") 
            else:
                print(f"| {" "} |", end="")
        print()

def verifica_vitoria(matriz, player):
    linhas = [-1, 0, +1]
    colunas = [-1, 0, +1]
    
    #Percorre cada indice da matriz
    for i in range(0, 6):
        for j in range(0, 10):
            if matriz[i][j] == player:
                contagem = 1
                
                print(j)
                
                #Testa todas as combinações de incremento
                for linha in linhas:
                    for coluna in colunas:
                        #verifica se os incrementos não estão fora do range e se a combinação de incrementos é (0, 0)
                        if (linha == 0 and coluna == 0) or \
                            (i + linha >= 6 or i + linha <= -1) or \
                            (j + coluna <= -1 or j + coluna >= 10):
                                
                            continue
                        #Verifica se o adjacente é igual ao player
                        elif matriz[i + linha][j + coluna] == player:
                            #Verifica as 3 celulas na direção da celula adjacente igual ao player
                            for x in range(1, 4): #[1, 2, 3]
                                linha_incrementada = i + (x * linha)
                                coluna_incrementada = j + (x * coluna)
                                        
                                #Valida se a linha/coluna incrementada está dentro do range da matriz
                                if (linha_incrementada >= 6) or (linha_incrementada <= -1) or \
                                    (coluna_incrementada >= 10) or (coluna_incrementada <= -1):
                                    contagem = 1
                                    break
                                #Verifica se a coordenada incrementada pertence ao player
                                elif matriz[linha_incrementada][coluna_incrementada] == player:
                                    contagem += 1
                                else:
                                    contagem = 1
                                    break
                                
                                #Valida vitória
                                if contagem == 4:
                                    return True
    return False
                                
#Inicio
init(autoreset=True)

print(f"{"-" * 10} Bem vindo ao LIG4! {"-" * 10}")

matriz = [[" " for i in range(0, 10)] for j in range(0, 6)]

player = 1
while True:
    
    print(f"\nÉ a vez do Player {player}:")
    
    exibir_matriz(matriz)
    
    resposta = False
    while resposta == False:
        while True:
            try:
                coluna = int(input("Escolha a sua coluna: "))
                if 1 <= coluna <= 10:
                    break
            except Exception as erro:
                print(f"ERRO: {erro}")
            print("A coluna selecionada não existe, por favor, selecione uma das colunas disponíveis.") if not(1 <= coluna <= 10) else None
        
        matriz, resposta = colocar_disco(coluna - 1, matriz, player)
        print("A coluna selecionada já está totalmente preenchida... escolha outra.") if resposta == False else None
        
    
    vitoria = verifica_vitoria(matriz, player)
    
    if vitoria:
        print(f"\nO Player {player} VENCEU!")
        
        exibir_matriz(matriz)
        break
    
    #Alterna entre os players
    if player == 1:
        player = 2
    else:
        player = 1