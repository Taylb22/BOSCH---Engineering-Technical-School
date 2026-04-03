import pandas as pd

path = "S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Bibliotecas Python/Pandas/CSV/BostonHousing.csv"

boston_db = pd.read_csv(path, sep=",")

print(boston_db.loc[:13, ["crim", "medv"]])