n = input("Vui lòng nhập một số: ")
tong = 0
i = 0
while i < len(n):
    tong += int(n[i])
    i += 1
print("Tổng các chữ số là:", tong)