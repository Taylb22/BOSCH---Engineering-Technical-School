import pandas as pd

df = pd.read_csv("CSVs/titanic.csv")

a = df.groupby('Sex').agg(
    media_idade=('Age', lambda x: x.mean()),
    vivos=('Survived', lambda x: (x==1).sum()),
    mortos=('Survived', lambda x: (x==0).sum())
)

print(a)
