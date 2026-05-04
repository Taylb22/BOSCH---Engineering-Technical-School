import pandas as pd

path = "S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Python/Bibliotecas Python/Pandas/Exercises/CSV/dados.csv"

df = pd.read_csv(path, sep=",", encoding='latin1')

house = df[(df["quartos"] == 3)
           & (df["bairro"] == "Tijuca")
           & (df["area"] > 130)].sort_values(by="preco",
                                             ascending=True).head(1)

print(house)