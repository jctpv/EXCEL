import pandas as pd
df = pd.read_excel("EXCEL_011.xls")
print(df.head(3))
pk = pd.read_csv("pokemon_data.csv")
print(pk.head(2))
pktxt = pd.read_csv("pokemon_data.txt", delimiter="\t")
print(pktxt.head(3))
print(df.columns)
print()