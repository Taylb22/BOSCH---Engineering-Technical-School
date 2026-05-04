import matplotlib.pyplot as plt
import pandas as pd

path = "../CSV/he.csv"
df =pd.read_csv(path, sep=",")

group = df.groupby("MachineId")["DefaultId"].count().reset_index()
print(group)

plt.bar(group["MachineId"], group["DefaultId"])
plt.show()