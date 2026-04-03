import pandas as pd

df = pd.read_csv('CSVs/dados.csv', sep=',', encoding='iso-8859-1')

df = df.loc[(df['quartos'] == 3) & (df['bairro'] == 'Tijuca') & (df['area'] > 130)].sort_values(by='preco')
print(df.head(1))
