a = [float(x) for x in input("Nhập vào vector a : ").split()]
b = [float(x) for x in input("Nhập vào vector b : ").split()]
dot_product = sum(a[i] * b[i] for i in range(len(a)))
print("Tích vô hướng của hai vector là:", dot_product)