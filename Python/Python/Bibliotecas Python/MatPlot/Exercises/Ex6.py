import matplotlib.pyplot as plt
import pandas as pd

path = "../CSV/california_housing_train.csv"
df = pd.read_csv(path, sep=",")

# def agrupamento(line):
#     opcoes = (
#         0,
#         100000,
#         200000,
#         300000,
#         400000,
#         500000
#     )
#     for i in range(len(opcoes) - 1):
#         if line["median_house_value"] >= opcoes[i + 1]:
#             continue
#         else:
#             return opcoes[i]
#     else:
#         return opcoes[-1]

# df["value"] = df.apply(agrupamento, axis=1)

# group = df["value"].value_counts().reset_index().sort_values(by="value", ascending=True)
# print(group)

# plt.plot(group["value"], group["count"], color="blue")
plt.hist(df["median_house_value"])

plt.show()