
try:
    num1 = int(input("Nhập số nguyên thứ nhất: "))
    num2 = int(input("Nhập số nguyên thứ hai: "))
    a, b = num1, num2
    while b != 0:
        temp = b
        b = a % b
        a = temp
    lcm = (num1 * num2) // a
    print("Bội số chung nhỏ nhất của", num1, "và", num2, "là:", lcm)
except ValueError:
    print("Bạn đã nhập không phải là số nguyên.")
