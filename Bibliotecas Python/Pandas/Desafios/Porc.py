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

def calculate_percentage(val, total):
    total = val / total
    return total * 100

def porc(linha):
    return (linha[""] / 891) * 100

path = "S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Bibliotecas Python/Pandas/CSV/titanic.csv"

df_titanic = pd.read_csv(path, sep=",")

# Familia = df_titanic[(df_titanic["SibSp"] > 0) | (df_titanic["Parch"] > 0)].count()
# Sem_Familia = df_titanic[(df_titanic["SibSp"] == 0) & (df_titanic["Parch"] == 0)].count()

# H_M = df_titanic[(df_titanic['Sex'] == "male") & (df_titanic["Survived"] == 0)].count()
# M_M = df_titanic[(df_titanic['Sex'] == "female") & (df_titanic["Survived"] == 0)].count()

# group = df_titanic[df_titanic["Survived"] == 0].groupby(df_titanic["Pclass"]).count()

new_column = df_titanic.apply(faixa_etaria, axis=1)
df_titanic["Faixa_Etaria"] = new_column

group_a = df_titanic.groupby(df_titanic["Faixa_Etaria"]).count()
group_a["Porcentagem"] = round(group_a["Survived"].div(group_a["Survived"].sum(), axis=0).multiply(100), 2)

print()
print(group_a[["Survived", "Porcentagem"]].sort_values(by="Porcentagem", ascending=False))
print()