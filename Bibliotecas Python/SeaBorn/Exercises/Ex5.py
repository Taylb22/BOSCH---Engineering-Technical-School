import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

path = "../../CSVs/tips.csv"

df = pd.read_csv(path, sep=';')
df.drop(['sex', 'smoker', 'day', 'time'], axis=1, inplace=True)

sns.heatmap(df.corr(), annot=True)
plt.show()