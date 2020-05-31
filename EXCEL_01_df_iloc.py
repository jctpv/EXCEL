import pandas as pd
df =  pd.read_csv("pokemon_data.txt")

print("------0------")
print(df.head())

df =  pd.read_csv("pokemon_data.txt", delimiter="\t")
print("------0.x------")
print(df.head())

print("------1------")
print(df.head(3))#até o index 2

print("------2------") #print columns heads
print(df.columns)#READ columns
print("------2.x------") #print index
print(df.index)#read index

print("------3------")
print(df["Name"])#print especifc column> formato [head da coluna][range do row]

print("------3.1------")
x=5
print(df["Name"][0:x])#print especifc column and index row range> formato [head da coluna][range do row]

print("------3.2------")
print(df["Name"][2])#print especifc column and especific row> formato [head da coluna][index do row]

print("------4.0------")# outra forma de print apenas a coluna Name> formato df.head[range do row]
print(df.Name)

print("------4.1------")# apenas a coluna Name> formato df.head[range do row]
print(df.Name[2:4])

print("------5------")#duas ou mais columns, tem que ser colocada em uma lista, não dá certo em tuple
print(df[["Name","Speed"]][0:3])

print("------5.1------")#duas ou mais columns, tem que ser colocada em uma lista, não dá certo em tuple
print(df[["Name", "Speed", "Type 1"]][0:3])

print("------iloc------")
print("------6.0------")# all row and column(iloc-> index location) formato -> [row]
print(df.iloc[3])
print("------6.1------")# all arow and column (iloc-> index location) formato -> [index row range][column range]
print(df.iloc[:][:])
print("------6.2------")# all arow and column (iloc-> index location)formato -> [index row range, column range]
print(df.iloc[:, :])

print("------7.0------")# iloc procura a row no index 1 e retorna cada item com a respectiva head da column
print(df.iloc[0])
print("------7.1------")#retorna cada item da row index 1 com a respctiva head da column no range de 0 a 1 das column
print(df.iloc[1][0:2])
print("------7.2------")#formato -> [index row range]
print(df.iloc[0:4])
print("------7.3------")#formato -> [index row range]
print(df.iloc[2:6])
print("------7.4------") #especific location [row, column]
print(df.iloc[2,2])
print("------7.4x------") #especific location [row][column]
print(df.iloc[2][2])

print("------7.5------") #especific range location [row range, column range)
print(df.iloc[1:4,1:4])
print("------7.6------") #especific location [rows, columns)
print(df.iloc[[1, 2, 4], [1, 3]])
print("------7.6x------") #especific location [rows, columns)
print(df.iloc[[2, 1, 4], [3, 1]])