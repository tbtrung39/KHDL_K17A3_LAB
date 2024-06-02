n = int(input("Nhập số: "))
a = 1
for i in range(1, n+1):
    k = 1
    for j in range(2, 2*i+2):
        k *= j / (j - 1)
    a += k
print("Kết quả của phép toán là:", round(a, 3))
