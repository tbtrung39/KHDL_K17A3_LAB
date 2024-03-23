x = float(input("Nhập giá trị x: "))
epsilon = 1e-4  # Sai số
cos_x = 1
term = 1
i = 0
factorial = 1

while term > epsilon or -term > epsilon:
    factorial *= (2*i+1)*(2*i+2)  # Tính giai thừa
    term *= -x*x / factorial  # Công thức truy hồi
    cos_x += term
    i += 1

print("Giá trị gần đúng của cos(", x, ") = ", cos_x)