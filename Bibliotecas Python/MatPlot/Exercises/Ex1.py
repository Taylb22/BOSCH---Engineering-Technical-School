import pandas as pd
import matplotlib.pyplot as plt

path = "../CSV/gols_pr.csv"

df = pd.read_csv(path, sep=',')

plt.plot(df.ano[df["clube"] == "coritiba"], df.gols_pro[df["clube"] == "coritiba"], color="green", label="coritiba")
plt.plot(df.ano[df["clube"] == "parana"], df.gols_pro[df["clube"] == "parana"], color="blue", label="parana")
plt.plot(df.ano[df["clube"] == "athletico-pr"], df.gols_pro[df["clube"] == "athletico-pr"], color="red", label="athletico")

plt.xlabel("Ano")
plt.ylabel("Gols")

plt.legend()
plt.show()