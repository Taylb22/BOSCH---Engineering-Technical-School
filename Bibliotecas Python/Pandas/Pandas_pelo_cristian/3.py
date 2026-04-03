import pandas as pd

df = pd.read_csv('CSVs/cat_breeds_clean.csv', sep=';')

#==============================================================
# a = df[df['Breed'] == 'Angora']
# print(a)
#==============================================================
# europe = ['England','France','Germany']
# b = df[df['Country'].isin(europe)]
# print(b)
#==============================================================
# c = df[df['Fur_colour_dominant'] == 'white']['Country'].unique().tolist()
# print(c)
#==============================================================
# d = df[df['Age_in_months'] > 6]
# d['ratio'] = d['Weight']/d['Body_length']
# print(d[['Age_in_months','Weight','Body_length','ratio']])
#==============================================================
# e = df[df['Gender']=='male']
# print(e[['Breed','Age_in_years','Weight']])
#==============================================================
# f = df[df['Breed'] == 'Ragdoll']
# f['Sleep_time_hours_per_day_percent'] = f['Sleep_time_hours'] / 24
# print(f[['Breed', 'Sleep_time_hours_per_day_percent']])
#==============================================================
# g = df['Body_length'].sum()
# print(g)
#==============================================================
# h = df['Sleep_time_hours'].mean()
# print(h)
#==============================================================
# i = df.loc[((df['Age_in_months'] > 3) & (df['Age_in_months'] < 12)), 'Weight'].sum()
# print(i)
#==============================================================
# j = df[(df['Fur_colour_dominant'] == 'white') | (df['Fur_colour_dominant'] == 'black')]
# j = j.groupby('Fur_colour_dominant').apply(
#     lambda g: (g['Body_length'] / g['Age_in_years']).mean()
# ).reset_index(name='ratio')
# print(j)
#==============================================================













# df.loc[
#     (df['A'] > 2) &
#     (df['B'] == 'o') &
#     (df['C'] == 1)
# ]