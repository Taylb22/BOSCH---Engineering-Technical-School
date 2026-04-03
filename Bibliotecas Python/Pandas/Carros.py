import pandas as pd

path = "S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Bibliotecas Python/Pandas/CSV/Cars93_miss.csv"

df_car = pd.read_csv(path, sep=",")

colunas = ["Manufacturer", "Make", "Price", "MPG.city", "Type", "Passengers"]
filtro = df_car["Passengers"] == 5

# df_filtrado = df_car[filtro].nlargest(10, ["MPG.city"]).nsmallest(5, ["Price"])
# print(df_filtrado[colunas].dropna().head())

# print()

df_filtrado = df_car[filtro].sort_values(by="MPG.city", ascending=False).sort_values(by="Price")
print(df_filtrado[colunas].dropna().head())