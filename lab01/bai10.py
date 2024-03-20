
n = int(input("Nhập số lần tung súc sắc (n): "))

# Xác suất để không có lần nào cả 3 súc sắc đều ra số 6
l = (5 / 6) ** n
    
# Xác suất để ít nhất một lần cả 3 súc sắc đều ra số 6
k = 1 - l

print(f"Xác suất để ít nhất một lần cả 3 súc sắc đều ra số 6 sau {n} lần tung là: {k:.2f}")
