import pandas as pd

def soma_sibsp_parch(linha):
    return linha["SibSp"] + linha["Parch"]

path = "S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Bibliotecas Python/Pandas/CSV/titanic.csv"

titanic = pd.read_csv(path, sep=",")

new_column = titanic.apply(soma_sibsp_parch, axis=1)

print(new_column)

titanic["Ralatives"] = new_column
print()
print(titanic)