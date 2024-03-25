# Nhập vào 2 vector a và b
a = [int(i) for i in input("Nhập vector a (các phần tử cách nhau bởi dấu cách): ").split()]
b = [int(i) for i in input("Nhập vector b (các phần tử cách nhau bởi dấu cách): ").split()]

# Tính tích vô hướng của 2 vector
tich_vh = 0
for i in range(len(a)):
    tich_vh += a[i] * b[i]

print("Tích vô hướng của hai vector là: ", tich_vh)
