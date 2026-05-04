import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lib import vdist_binomial

df = pd.read_csv("CSVs/transacoes_fraude.csv", sep=',')
print(f"Proporção de transações fraudulentas -> {(df.fraude[df.fraude == 1].count() / df.fraude.count()):.2%}")
df["suspeita"] = np.where(((df.tentativas_login > 3) | (df.falha_login == 1)), 1, 0)

fig, axis = plt.subplots(nrows=1, ncols=2)
fraude = df.value_counts("fraude")
suspeita = df.value_counts("suspeita")
axis[0].bar(["Não Fraude", "Fraude"], fraude)
axis[1].bar(["Não Suspeita", "Suspeita"], suspeita)
plt.show()

#A taxa de fraudes é relativamente baixa, e o número de suspeitas é muito maior do que a realidade de fraudes.