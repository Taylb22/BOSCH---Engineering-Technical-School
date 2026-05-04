import pandas as pd

path = "S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Python/Bibliotecas Python/Pandas/Exercises/CSV/master.csv"

df = pd.read_csv(path, sep=",")
df = df.drop("HDI for year", axis=1)

filtered = df[(df["country"] == "Brazil")
              & (df["year"] == 1987)
              & (df["sex"] == "female")
              & (df["generation"] == "Boomers")]

print(filtered)