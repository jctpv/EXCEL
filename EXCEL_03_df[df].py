import pandas as pd
print("------0------")
df = pd.read_excel("EXCEL_011.xls")
valor = 10

print("------------------------------------1------------------------------------------------")
print(df[["A", "B"]])

print("------------------------------------1.1------------------------------------------------")
print(df["A"] > valor)

print("------------------------------------1.2------------------------------------------------")
print(df[df["A"] > valor])

print("------------------------------------1.3------------------------------------------------")
print(df[df["A"] % 2 == 0])

print("------------------------------------1.4------------------------------------------------")
print(df[df[["A", "B"]] % 2 == 0])

print("------------------------------------1.4------------------------------------------------")
print(df["A"])
