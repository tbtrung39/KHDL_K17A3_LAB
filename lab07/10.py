m = int(input("Nhập số tự nhiên m: "))
n = int(input("Nhập số tự nhiên n: "))
a = str(m)
b = str(n)
x = set()
y = 0
for digit in a:
    if digit not in x:
        if digit in b:
            x.add(digit)
            y += int(digit)
print("Tổng các chữ số chung của", m, "và", n, "là:", y)
