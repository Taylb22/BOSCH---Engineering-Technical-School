import pandas as pd

def calculate_percentage(val, total):
    value = val / total
    return value * 100

path = "S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Bibliotecas Python/Pandas/CSV/titanic.csv"

df_titanic = pd.read_csv(path, sep=",")

total = df_titanic["Survived"].count()
dead = df_titanic[df_titanic["Survived"] == 0].count()
alive = df_titanic[df_titanic["Survived"] == 1] .count()

print(f"TOTAL = {total}")
print(f"DEAD = {dead} | {calculate_percentage(dead, total)}")
print(f"ALIVE = {alive} | {calculate_percentage(alive, total)}")