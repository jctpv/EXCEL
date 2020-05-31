import pandas as pd
df = pd.read_excel("EXCEL_011.xls")

print("------0------")
print(df.iterrows())
print("------0.------")
nxt = next(df.iterrows())#somente para verificar a função next
print(nxt)
print("------0.0------")
nxt0 = next(df.iterrows())[0]# o uso dos couchete serve para especificar no tuple (index, series) sendo 0 ou 1
print(nxt0)
print("------0.1------")
nxt1 = next(df.iterrows())[1]
print(nxt1)

print("------01------") #print cada item da row com a respectiva head columns, todas as column
for each in df.iterrows():
    print(each)

print("------02------")#print a linha com a respectiva head,, todas as column
for index, row in df.iterrows():
    print(index, row)
print("------02.1------")  # mesmo que anterior, so que que retornando o segundo item do tupple (index, series)
for (index, row) in df.iterrows():
    print(row)
print("------02.2------")  # mesmo que anterior, so que que retornando a primeira columns
for (index, row) in df.iterrows():
    print(row[0])
print("------02.3------")  # mesmo  que anterior, so que que retornando a primeira columns
for (index, row) in df.iterrows():
    print(row[1])

print("------11.2------") ##print as column selecionadas de cada row, , todas as column de B a A
for (index, row) in df.iterrows():
    print(index, row["A"])
print("------11.3------") ##print as column selecionadas de cada row, , todas as column de B a A
for (index, row) in df.iterrows():
    print(index, row[["B", "A"]])
print("------11.4------") ##print as column selecionadas de cada row, todas as column de 1 a 3 "B a C"
for (index, row) in df.iterrows():
    print(index, row[1:3])
print("------11.5------") ##print a  row e a column selecionada na sequencia
for (index, row) in df.iterrows():
    print(index, row["B"],row["A"])