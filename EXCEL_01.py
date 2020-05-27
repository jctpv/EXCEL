import pandas as pd
print("------0------")
df = pd.read_excel("EXCEL_011.xls")
print("------1------")
print(df.head())

print("------2------")
pk = pd.read_csv("pokemon_data.csv")
print(pk.head(2))

print("------3------")
pktxt = pd.read_csv("pokemon_data.txt", delimiter="\t")
print(pktxt.head(3))

print("------4------")
#READ columns
print(df.columns)

print("------5------")
x=5
print(df["A"][0:x])

print("------6------")
print(df.A)

print("------7------")
print(df["E"])

print("------8------")
print(df.B)

print("------9------")
#duas ou mais columns, tem que ser colocada em uma lista, não dá certo em tuple
print(df[["A", "E"]])

print("------10------")
# iloc procura a linha e retorna com o head da coluna (iloc-> index location)
print(df.iloc[1])
print("------10.1------")
print(df.iloc[0:4])
print("------10.2------")
print(df.iloc[2:6])
print("------10.3------") #especific location [row, column)
print(df.iloc[2,2])

print("------11.1------") #print a linha com a respectiva head columns, todas as column
for each in df.iterrows():
    print(each)
print("------11.2------")#print a linha com a respectiva head,, todas as column
for index, row in df.iterrows():
    print(index, row)
print("------11.3------") ##print as column selecionadas de cada row, , todas as column de B a A
for (index, row) in df.iterrows():
    print(index, row[["B", "A"]])
print("------11.4------") ##print as column selecionadas de cada row, todas as column de 1 a 3 "B a C"
for (index, row) in df.iterrows():
    print(index, row[1:3])
print("------11.5------") ##print a row e a column selecionada na sequencia
for (index, row) in df.iterrows():
    print(index, row["B"],row["A"])