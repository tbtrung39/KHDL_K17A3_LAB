try:
    so1 = int(input("Nhập số nguyên thứ nhất: "))
    so2 = int(input("Nhập số nguyên thứ hai: "))
    a, b = so1, so2
    while b:
        a, b = b, a % b
    bcnn = so1 * so2 // a
    print("Bội chung nhỏ nhất của", so1, "và", so2, "là:", bcnn)
except ValueError:
    print("Vui lòng nhập vào số nguyên.")
