import typing

def open_matrix(file):
    matriz = []
    with open(file, 'r') as arquivo:
        # arquivo = arquivo.read()
        # linha = []
        
        # for char in range(len(arquivo)):
            # if arquivo[char] == "[":
        for line in arquivo.readlines():
            # print(line)
            # line.strip()
            aux = line.split(' ')
            # print(aux)
            new_line = []
            for item in aux:
                if item != '':
                    new_line.append(int(item))
            matriz.append(new_line)
                    # if arquivo[i] == ']':
                    #     matriz.append(linha.copy())
                    #     linha.clear()
                    #     break
                    # if arquivo[i].isnumeric():
                    #     linha.append(int(arquivo[i]))
        
        return matriz

memo = {}
def find_best(cities : list[list[int]], history : list) -> list:
    current = history[-1]
    
    # key = (history, current)

    # if key in memo:
    #     route, sum = memo[key]
    #     return route, sum

    if len(history) == len(cities):
        result = [current, history[0]]
        sum = cities[current][history[0]]
        return result, sum

    results = {}
    for i in range(len(cities[current])):
        if not(i in history):
            route, sum = find_best(cities, history + [i])
            results[i] = (route, sum)
    
    best_route = None
    best_sum = float('inf')
    for i in results.keys():
        if results[i][1] < best_sum:
            best_route = results[i][0]
            best_sum = results[i][1]

    route = [current] + best_route
    sum = cities[current][route[1]] + best_sum
    # memo[key] = (route, sum)
    return route, sum

def TSP(cities : list[list[int]], start : int) -> list:
    memo.clear()
    start -= 1
    route, sum = find_best(cities, [start])

    for i in range(len(route)):
        route[i] += 1

    return route, sum

matrix = open_matrix("S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Python/Projeto/b.txt")
for row in matrix:
    print(row)
print()

route, sum = TSP(matrix, start=1)
print(f"ROTA -> {route}\nSOMA -> {sum}")