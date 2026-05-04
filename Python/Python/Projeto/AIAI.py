import typing

def open_matrix(file): #função para ler o arquivo.txt do problema
    matriz = []
    with open(file, 'r') as arquivo:
        for line in arquivo.readlines():
            aux = line.split(' ')
            new_line = []
            for item in aux:
                if item != '':
                    new_line.append(int(item))
            matriz.append(new_line)

        
        return matriz

#memo = {(mask, current) : (ans, route)} -> Estrutura do nosso memoization
memo = {}
def find_best(cities : list[list[int]], mask : int, current : int, start=0) -> list:
    key = (mask, current) #Formulando a chave
    
    if key in memo: #Evitando cálculo redundante com memoization
        ans, route = memo[key]
        return ans, route

    
    n = len(cities)

    if mask == 2**n - 1: #verificando se todas as cidades já foram visitadas
        ans = cities[current][start]
        route = [current + 1] + [start + 1]
        memo[key] = (ans, route) #memorização da rota
        return ans, route
    
    route = None
    ans = float('inf')
    for i in range(len(cities[current])): #percorrendo todas as rotas possíveis a partir da cidade atual
        if not(mask >> i & 1 == 1): #verificando se a a cidade a se visitar ainda não foi visitada
            mask = mask | 1 << i #atribuindo a cidade como "visitada"
            s, r = find_best(cities, mask, current=i, start=start) #recursividade para explorar a rota
            if cities[current][i] + s < ans: #verificando se a rota encontrada é a melhor até agora
                ans = cities[current][i] + s #soma da rota
                route = [current + 1] + r #a rota em si
            mask = mask ^ 1 << i #backtracking

    memo[key] = (ans, route) #memorização da rota
    return ans, route

def TSP(cities : list[list[int]], start=1) -> list: #Função "Máscara", função temporária que só serve para tornar mais fácil para o usuário
    memo.clear()
    start -= 1 #padronização, pois o codigo utiliza o indice, porém, a intenção é que o usuário indique o número da cidade em si
    mask = 0 >> len(cities) - 1 #Máscara (em Bits) que armazena "true" e "false" para identificar quais cidades foram visitadas
    mask = mask | 1 << start #Operação "or" para definir que a cidade inicial já foi visitada
    ans, route = find_best(cities, mask, current=start, start=start)

    return ans, route

matrix = open_matrix("S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Python/Projeto/26_cidades.txt")
for row in matrix:
    print(row)
print()

sum, route = TSP(matrix, start=1) #Defina de qual cidade deseja partir (o parametro "start" não é indexado)
print(f"ROTA -> {route}\nSOMA -> {sum}")