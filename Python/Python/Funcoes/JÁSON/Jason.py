def read_list() -> dict:
    pass

def read_dict(data : str, end : int, start=0) -> dict:
    dict = {}
    
    data = list(data)
    is_key = True
    is_str = True
    key = []
    value = []
    for i in range(end):
        if data[i] == ':':
            is_key = False
            continue
        if data[i] == ',' or i == end - 1:
            k = ''.join(key)
            v = ''.join(value)
            dict[k] = v
            
            key.clear()
            value.clear()
            is_key = True
            continue
        
        if is_key:
            if is_str and not(data[i] == "\""):
                key.append(data[i])
            elif not(is_str):
                key.append(data[i])
        else:
            if is_str and not(data[i] == "\""):
                value.append(data[i])
            elif not(is_str):
                value.append(data[i])
            
        if data[i] == "\"" and is_str:
            is_str = False
        elif data[i] == "\"" and not(is_str):
            is_str = True
    
    return dict

def read_json(data) -> dict:
    with open(data, "r") as lendo:
        data = lendo.read()

    data = data.strip()
    data = data.replace('\n', '')
    data = data.split()
    data = ''.join(data)
    
    size = len(data)
    
    jasom = read_dict(data[1:size], size - 1)

    return jasom

dados = read_json("S:\COM\Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Python/Funcoes/JÁSON/t1.json")

print(dados)
print(dados['4'])