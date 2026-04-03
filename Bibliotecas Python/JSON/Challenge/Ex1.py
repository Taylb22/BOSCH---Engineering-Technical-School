import json
import typing

def group_by(data : list[dict[str, typing.Any]], by : str, on : str):
    result = []
    uniques = []
    
    for row in data:
        if not row[by] in uniques:
            uniques.append(row[by])
            result.append({by : row[by], on : row[on]})
            continue
        
        for line in result:
            if line[by] == row[by]:
                line[on] += row[on]
                break
    return result

def top(data : list[dict[str, typing.Any]], on : str):
    t = data[0]
    for row in data: 
        if row[on] > t[on]:
            t = row
    return t

def sum_col(data : list[dict[str, typing.Any]], on : str):
    S = 0
    for row in data:
        S += row[on]
    return S

path = "data.json"
with open(path, "r", encoding='utf-8') as file:
    data = json.load(file)

group_vendors = group_by(data["vendas"], by="vendedor", on="valor")
group_products = group_by(data["vendas"], by="produto", on="valor")

total_vendas = sum_col(data["vendas"], on="valor")
melhor_produto = top(group_products, on="valor")["produto"]
melhor_vendedor = top(group_vendors, on="valor")["vendedor"]

print(f"\ntotal_vendas: {total_vendas}\nproduto mais vendido: {melhor_produto}")
for row in group_vendors: print(f"total de vendas {row["vendedor"]}: {row["valor"]}")
print(f"melhor vendedor: {melhor_vendedor}\n")

report = {
    "total_vendas" : total_vendas,
    "produto_mais_vendido" : melhor_produto,
    "melhor_vendedor" : melhor_vendedor
}

with open("report.json", "w") as file:
    json.dump(report, file, indent=4)