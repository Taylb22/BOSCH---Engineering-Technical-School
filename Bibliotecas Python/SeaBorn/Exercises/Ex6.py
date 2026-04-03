import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

path = "../../CSVs/tips.csv"

df = pd.read_csv(path, sep=';')

g = sns.FacetGrid(data=df, col='time')
g.map(sns.histplot, 'total_bill')
plt.show()