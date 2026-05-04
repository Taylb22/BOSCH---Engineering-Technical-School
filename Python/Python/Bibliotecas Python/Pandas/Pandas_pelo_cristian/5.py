import pandas as pd

df = pd.read_csv('CSVs/master.csv', sep=',', encoding='iso-8859-1')

def country(column):
    return column[:-4]
def year(column):
    return column[-4:]

a = df[:]
a['country'] = a['country-year'].apply(country)
a['year'] = a['country-year'].apply(year)
#==============================================================
a = a.drop(columns=['HDI for year'])
#==============================================================
a = a.loc[
    (a['country'] == 'Brazil') & 
    (a['year'] == '1987') & 
    (a['sex'] == 'female') & 
    (a['generation'] == 'Boomers') 
]
#==============================================================
print(a)