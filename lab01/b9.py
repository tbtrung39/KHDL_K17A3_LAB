n = int(input("Nhập số lần tung xúc sắc: "))
p = 1 - (5/6) ** (3 * n)
print("Xác suất để ít nhất một lần trong", n, "lần tung cả ba xúc sắc đều ra số 6 là:", round(p, 2))