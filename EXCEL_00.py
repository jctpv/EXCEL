import pandas as pd

print("------0------")
df = pd.read_excel("EXCEL_011.xls")
print("------1------")
print(df.head())# tudo

print("------2------")
pk = pd.read_csv("pokemon_data.csv")
print(pk.head(2))#até o index 1

print("------3------")
pktxt = pd.read_csv("pokemon_data.txt", delimiter="\t")#separa pelo delimitador do banco de dados
print("------3.1------")
print(pktxt.head())#
print("------3.2------")
print(pktxt.head(3))#até o index 2
print("------3.3------") #print index  and heads
print(pktxt.index)
print(pktxt.columns)

print("------4------")
print(df.columns)#READ columns
print(df.index)#read index

print("------5------")
x=5
print(df["A"][0:x])#print especifc column and index range

print("------6------")# apenas a coluna A
print(df.A)

print("------7------")#outra maneira de print uma coluna especifica
print(df["D"])

print("------8------")
print(df.B[0:3])

print("------9------")#duas ou mais columns, tem que ser colocada em uma lista, não dá certo em tuple
print(df[["A","D"]][0:3])

print("------9.1------")#duas ou mais columns, tem que ser colocada em uma lista, não dá certo em tuple
print(df[["A", "D", "B"]][0:3])
