import pandas as pd
import numpy as np
from lib import vdist_binomial

df = pd.read_csv("CSVs/transacoes_fraude.csv", sep=',')
# df["suspeita"] = np.where(((df.tentativas_login > 3) | (df.falha_login == 1)), 1, 0)

n = df.fraude.count()
p = df.fraude[df.fraude == 1].count() / n

x = np.arange(0, 5)
print(vdist_binomial(n, x, p))
