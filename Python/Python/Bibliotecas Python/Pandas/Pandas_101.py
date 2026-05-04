import pandas as pd

path = "S:/COM/Human_Resources/01.Engineering_Tech_School/02.Internal/5 - Aprendizes/5 - Análise de dados/2 - Análise de dados 2025/Henrique dos Santos/Bibliotecas Python/Pandas/CSV/titanic.csv"

titanic_db = pd.read_csv(path, sep=",") # Leitura do CSV

# print(type(titanic_db))
# print()
# print(titanic_db.head()) # Printa os primeiros 5 elementos | Pode aceitar paramentros do quantos quer exibir
# print()
# print(titanic_db.tail()) # Printa os últimos 5 elementos | Pode aceitar paramentros do quantos quer exibir

print()

# print(titanic_db["Name"].head()) # Acessa o "Head" apenas da coluna "Nome"
# print()
# print(titanic_db.Name.tail()) # Acessa o "Tail" apenas da coluna "Nome"

# print(titanic_db.shape) # Mostra as dimensões do db
# print(titanic_db.index) # Mostra o range do index
# print(titanic_db.columns) # Mostra os nomes das colunas
# print(titanic_db.dtypes) # Mostra os tipos de dados das colunas

# filtro_tipo_num = (titanic_db.dtypes != "object")
# print(filtro_tipo_num)

# colunas_num = titanic_db.dtypes[filtro_tipo_num].index
# print(colunas_num)
# print()
# print(titanic_db[colunas_num[0:-2]].head())
# print()

# print(titanic_db.head())
# print()
# cols = titanic_db.columns
# print(titanic_db[cols[:-1]].head())

# print(titanic_db.iloc[:, :-1].head())
# print()
# print(titanic_db.iloc[15:, :3].head())
# print()

# print(titanic_db.loc[:5, ["Survived"]])
# print()

# print(titanic_db.describe())
# print()
# print(titanic_db["Age"].describe())
# print()
# print(titanic_db.describe(include="all"))
# print()

# print(titanic_db.columns)
# print(titanic_db[["Age", "Pclass"]].describe())
# print()
# print(titanic_db[["Age", "Pclass"]].mean())
# print()
# print(titanic_db.loc[:6,["Age", "Pclass"]])
# print()
# print(titanic_db.loc[:6, ["Age", "Pclass"]].quantile(0.25))
# print()

print(titanic_db.shape)
print(titanic_db.isna().sum())
x = titanic_db.dropna()
print()
print(x.shape)
print()