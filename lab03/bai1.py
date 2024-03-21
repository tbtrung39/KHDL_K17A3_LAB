tong = 1
n = int(input("Nhập giá trị của n: "))
for i in range(0, n + 1):
    tich = 1
    for j in range(0, i + 1):
        tich = tich * ((2*(j + 1))/(2 * j + 3))
    tong = tong + tich
print("Tổng của dãy số là:",tong) 