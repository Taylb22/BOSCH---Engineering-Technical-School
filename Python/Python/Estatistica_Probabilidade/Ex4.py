import pandas as pd
import numpy as np
import math as m
# from lib import vComb

df = pd.read_csv("CSVs/transacoes_fraude.csv", sep=',')
# df["suspeita"] = np.where(((df.tentativas_login > 3) | (df.falha_login == 1)), 1, 0)

print(f"Combinatória de 5 transações -> {m.comb(df.fraude.count(), 5)}")
print(f"Combinatória de 5 contendo 2 fraudes -> {m.comb(df.fraude[df.fraude == 1].count(), 2) * m.comb(df.fraude[df.fraude == 0].count(), 3)}")