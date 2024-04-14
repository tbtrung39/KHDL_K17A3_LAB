X = int(input("Nhập giá trị X: "))
Y = int(input("Nhập giá trị Y: "))
array_2d = []

for i in range(X):
    row = []
    for j in range(Y):
        row.append(i * j)
    array_2d.append(row)
for row in array_2d:
    print(row)
