import pandas as pd

df = pd.read_csv('CSVs/tips.csv', sep=';', encoding='iso-8859-1')

df['tip_pct'] = df['tip'] / df['total_bill']
#==================================================
df.sort_values(by='tip_pct', ascending=False).head(1)
#==================================================
df.groupby('sex').agg(
    tip_mean=('tip', lambda x: x.mean())
)
#==================================================
# print(df['servings'].sum())
#==================================================
df['tipo de cliente'] = None
mean_tip = df['tip'].mean()
print(mean_tip)
df.loc[df['tip'] < mean_tip, 'tipo de cliente'] = 'pagador ruim'
df.loc[df['tip'] == mean_tip, 'tipo de cliente'] = 'pagador'
df.loc[df['tip'] > mean_tip, 'tipo de cliente'] = 'pagador bão'
# print(df[['tip', 'tipo de cliente']])
#==================================================
a = df.groupby('day').agg(
    clientes_ruim=('tipo de cliente', lambda x:(x=='pagador ruim').sum())
).sort_values(by='clientes_ruim', ascending=False)
print(a)
