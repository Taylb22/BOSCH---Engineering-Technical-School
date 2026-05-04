import matplotlib.pyplot as plt
import pandas as pd

path = "S:\COM\Human_Resources\01.Engineering_Tech_School\02.Internal\5 - Aprendizes\5 - Análise de dados\2 - Análise de dados 2025\Henrique dos Santos\Python\Bibliotecas Python\MatPlot\CSV\he.csv"
df =pd.read_csv(path, sep=",")

group = df.value_counts("is_corrective").reset_index()
print(group)

plt.pie(group["count"], labels=["Não Corretiva", "Corretiva"])
plt.show()