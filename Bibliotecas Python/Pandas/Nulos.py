import pandas as pd

path = "S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Bibliotecas Python/Pandas/CSV/titanic.csv"
titanic = pd.read_csv(path, sep=",")

y = titanic['Age'].fillna(titanic["Age"].mean())
print(titanic["Age"].head(15))
print(titanic.shape)
print()
print(y.head(15))
print(y.shape)
print()