import pandas as pd

path = "S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Bibliotecas Python/Pandas/CSV/titanic.csv"

df_titanic = pd.read_csv(path, sep=",")
# df_titanic["Died"] = 1 if df_titanic["Survived"] == 0 else 0
df_titanic = df_titanic["Survived"].groupby(df_titanic["Pclass"]).describe().iloc[:,:2]
df_titanic["mean"] = round(df_titanic["mean"] * 100, 2)

print(df_titanic)