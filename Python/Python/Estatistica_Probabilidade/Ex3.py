import pandas as pd
import numpy as np

df = pd.read_csv("CSVs/transacoes_fraude.csv", sep=',')
df["suspeita"] = np.where(((df.tentativas_login > 3) | (df.falha_login == 1)), 1, 0)

P = df[(df.suspeita == 1) & (df.fraude == 1)].count().suspeita / df.fraude[df.fraude == 1].count()
print(df.fraude[df.fraude == 1].count())

print(f"Probabilidade de ser fraude dado que é suspeita -> {((P * df.fraude[df.fraude == 1].count()) / df.suspeita[df.suspeita == 1].count()):.2%}")
print(f"Probabilidade geral de fraudes -> {(df.fraude[df.fraude == 1].count() / df.fraude.count()):.2%}")

#O indice de suspeita não esta se demontrando eficiente para detectar fraudes