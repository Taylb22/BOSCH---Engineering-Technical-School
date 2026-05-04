import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

path = "../../CSVs/flights.csv"

df = pd.read_csv(path, sep=',')
print(df)

sns.barplot(x='passengers', y='month', data=df, errorbar=None, palette="muted")
plt.show()