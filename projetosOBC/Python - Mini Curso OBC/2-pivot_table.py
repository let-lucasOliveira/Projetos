import pandas as pd

data = pd.read_excel("data/VendaCarros.xlsx")
# print(data)

df = data [["Fabricante", "ValorVenda", "Ano"]]
# print(df)

# 1- Criando a tabela pivô/tabela dinâmica
pivot_tabe = df.pivot_table(
    index="Ano",
    columns="Fabricante",
    values="ValorVenda",
    aggfunc="sum"
)

print(pivot_tabe)

# 2- Exportando tabela pivô em arquivo xlsx
pivot_tabe.to_excel("data/pivot_table.xlsx", "Relatorio")