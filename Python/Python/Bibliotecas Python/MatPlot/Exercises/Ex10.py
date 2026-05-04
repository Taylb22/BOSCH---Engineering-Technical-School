import matplotlib.pyplot as plt
import pandas as pd

path = "../CSV/he.csv"
df =pd.read_csv(path, sep=",")

group = df.value_counts("responsible").reset_index()
print(group)

plt.pie(group["count"], labels=group["responsible"])
plt.show()