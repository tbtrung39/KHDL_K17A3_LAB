so = int(input("Nhập một số nguyên dương: "))
tong = 0

while so > 0:
    tong += so % 10
    so //= 10
print("Tổng các chữ số của số vừa nhập là:", tong)
