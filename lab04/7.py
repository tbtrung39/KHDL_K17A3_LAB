a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = max(a, b)
while True:
    if c % a == 0 and c % b == 0:
        d = c
        break
    c += 1
print("Bội chung nhỏ nhất của", a, "và", b, "là:", d)
