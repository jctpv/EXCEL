mylist = iter(["apple", "banana", "cherry", "abacate", "abil", "jaca"])
print("------------00-------------------")
a = next(mylist)[2:6][1]
print(a)

print("------------01-------------------")
b = next(mylist)
a = next(mylist)
print(b)
print(a)

print("------------02-------------------")
c = next(mylist)
b = next(mylist)
a = next(mylist)
print(c)
print(b)
print(a)

print("-------------03--------------------")

dfx = pd.DataFrame([[1, 1.5],[2, 3]], columns=['int', 'float'])
print(dfx)
row = next(dfx.iterrows())[1]
print(row)
row = next(dfx.iterrows())[1]
print(row)

