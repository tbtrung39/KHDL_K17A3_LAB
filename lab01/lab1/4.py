x = float(input("Nhập giá trị của x: "))

tử_số = -x + (x**2 + 4)**0.5
mẫu_số = (x**4 + 1)**(1/7)
kết_quả = tử_số / mẫu_số

print(round(kết_quả, 2))