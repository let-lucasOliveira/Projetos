import pandas as pd

# 1- Importando dados
data = pd.read_excel("data/VendaCarros.xlsx")

# 2- Lista os primeiros registros
# print(data.head())

#3- Contagem de valores por Fabricante
print(data["Fabricante"].value_counts())