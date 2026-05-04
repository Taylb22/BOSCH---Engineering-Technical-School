import pandas as pd

path = "S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Python/Bibliotecas Python/Pandas/Exercises/CSV/train.csv"

df = pd.read_csv(path, sep=",")

group = df["PassengerId"].groupby(df["Sex"]).count().reset_index().sort_values(by="PassengerId", ascending=False)
group["Percentage"] = round(group["PassengerId"].div(group["PassengerId"].sum(), axis=0).multiply(100), 2)
group["Percentage"] = group["Percentage"].astype({"Percentage": str})
group["Percentage"] = group["Percentage"] + " %"

print(group[["Sex", "Percentage"]])