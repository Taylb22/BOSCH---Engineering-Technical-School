import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

path = "../CSVs/clientes.csv"

df = pd.read_csv(path, sep=",")
df = df.rename(columns={"Regiao" : "Cidade"})
df = df.drop(columns=["ID Cliente", "Data Cadastro"])
df["Nome"] = df["Nome"] + " " + df["Sobrenome"]
df.drop(columns="Sobrenome", inplace=True)

df["Situacao"] = df.Saldo.apply(lambda x: "Ativo" if x > df.Saldo.mean() else "Inativo")
df["Fiel"] = df.apply(lambda x: random.choice([True, False]), axis=1)

for sit in df.Situacao.unique():
    men = df[(df.Sexo == "Masculino") & (df.Situacao == sit)]
    women = df[(df.Sexo == "Masculino") & (df.Situacao == sit)]

    print(f"Relatório dos Clientes {sit}s")
    for cla in df.Classificacao.unique():
        auxM = men[men.Classificacao == cla]
        auxW = women[women.Classificacao == cla]
        
        avrM = np.round(auxM[auxM.Fiel == True].Fiel.count() / auxM.Fiel.count() * 100, decimals=2)
        avrW = np.round(auxW[auxW.Fiel == True].Fiel.count() / auxW.Fiel.count() * 100, decimals=2)
        
        print(f"Homen de classe {cla[:-1]}a que é cliente fiel: {avrM} %")
        print(f"Mulher de classe {cla[:-1]}a que é cliente fiel: {avrM} %")
    print("\n")
    
x = sns.catplot(data=df, x="Situacao", hue="Situacao",kind="count", col="Classificacao", row="Sexo")
x.set_axis_labels(x_var="Situação", y_var="Quantidade")

plt.show()
    
    