a = int(input("Nhập hệ số a: "))
b = int(input("Nhập hệ số b: "))
c = int(input("Nhập hệ số c: "))
x = -b/(2*a)
delta = b**2 -4*a*c
y = -delta / (4*a)
print("Đỉnh pt bậc 2 là: ", round(x,2), ";", round(y,2))
