n = int(input("Nhập vào một số nguyên dương: "))
s = 0
while n >0:
    i = n%10
    s += i
    n //=10
print(f'Tổng các chữ số đã nhập là: {s}')