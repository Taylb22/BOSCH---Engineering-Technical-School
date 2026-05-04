import pandas as pd
import numpy as np

df = pd.read_csv("CSVs/transacoes_fraude.csv", sep=',')
df["suspeita"] = np.where(((df.tentativas_login > 3) | (df.falha_login == 1)), 1, 0)

print(f"Probabilidade de ser suspeita dada que é uma fraude -> {(df[(df.suspeita == 1) & (df.fraude == 1)].count().suspeita / df.fraude[df.fraude == 1].count()):.2%}")
print(f"Probabilidade de ser suspeita dada que não é fraude -> {(df[(df.suspeita == 1) & (df.fraude == 0)].count().suspeita / df.fraude[df.fraude == 0].count()):.2%}")