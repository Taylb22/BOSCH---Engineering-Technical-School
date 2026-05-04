import matplotlib.pyplot as plt
import pandas as pd

path = "../CSV/he.csv"
df =pd.read_csv(path, sep=",")

df["end_date"] = pd.to_datetime(df["end_date"])
group = df.value_counts("end_date").reset_index().sort_values(by="end_date", ascending=True)
print(group)

plt.bar(group["end_date"], group["count"])
plt.xticks(rotation= 45)
plt.show()