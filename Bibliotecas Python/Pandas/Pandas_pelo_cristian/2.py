import pandas as pd

df = pd.read_csv('CSVs/train.csv')

a = df.groupby('Sex').agg(
    Proporcao = ('PassengerId', lambda x: len(x)/len(df))
)

print(a)