import pandas as pd



def faixa_etaria(linha):
    if linha["Age"] < 12:
        return "Criança"
    elif linha["Age"] >= 12 and linha["Age"] < 18:
        return "Adolescente"
    elif linha["Age"] >= 18 and linha["Age"] < 65:
        return "Adulto"
    elif linha["Age"] >= 65:
        return "Idoso"
    else:
        return None

path = "S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Bibliotecas Python/Pandas/CSV/titanic.csv"

df_titanic = pd.read_csv(path, sep=",")

new_column = df_titanic.apply(faixa_etaria, axis=1)

df_titanic["Faixa_Etaria"] = new_column

ai = df_titanic["Faixa_Etaria"].groupby(df_titanic["Faixa_Etaria"]).count()
b = ai.apply(porc)
ai["AA"] = b

print(ai)