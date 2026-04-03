import pandas as pd

path = "S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Bibliotecas Python/Pandas/CSV/titanic.csv"

df_titanic = pd.read_csv(path, sep=",")

filtros = ((df_titanic["Embarked"] == "S") 
           & (df_titanic["Pclass"] == 2)
           & (df_titanic["Age"] == 29)
           & (df_titanic["Sex"] == "female")
           & (df_titanic["Name"].str.contains("Anne", case=False))
           )

df_titanic = df_titanic[filtros]

if len(df_titanic["Name"].values) > 1:
    print(df_titanic)
else:
    nome = df_titanic["Name"].values

    if df_titanic["Sex"].values[0] == "Male":
        inicial = "O Homem procurado"
    else:
        inicial = "A Mulher procurado"

    if df_titanic["Survived"].values[0] == 1:
        final = "Sobreviveu"
    else:
        final = "Não Sobreviveu"
        
    print()
    print(f"{inicial} é, {nome[0]} e {final}")
    print()