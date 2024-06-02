x = float(input("Nhập x: "))
error = 1e-4

cos_x, term, n = 1, 1, 0
while abs(term) > error:
    term *= -x*x / ((2*n+1)*(2*n+2))
    cos_x += term
    n += 1

print("Giá trị của cos(", x, ") là", cos_x)
