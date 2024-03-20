# Nhập vào vector a
a = [float(i) for i in input("Nhập vào các phần tử của vector a, cách nhau bởi dấu phẩy: ").split(',')]

# Nhập vào vector b
b = [float(i) for i in input("Nhập vào các phần tử của vector b, cách nhau bởi dấu phẩy: ").split(',')]

# Tính tích vô hướng
tich_vh = 0
for i in range(len(a)):
    tich_vh += a[i] * b[i]

print("Tích vô hướng của hai vector là: ",tich_vh)
