x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
column = []
for i in range(0,x):
    row = []
    for j in range(0,y):
        result = i*j
        row.append(result)
    column.append(row)
print(column)