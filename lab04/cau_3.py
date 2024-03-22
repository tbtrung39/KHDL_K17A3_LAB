import math

x = math.radians(float(input("nhập gia trị x:")))
n = 0
term = 1
sum = term

while abs(term) > 1e-4:
    n += 1
    term *= -x**2 / ((2*n-1)*(2*n))
    sum += term

print(f"Giá trị gần đúng của cos({math.degrees(x)}) sử dụng khai triển Taylor là {sum}")
