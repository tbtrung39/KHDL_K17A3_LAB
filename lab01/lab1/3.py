pi = 3.14
r = float(input("Nhập bánh kính R là: "))
h = float(input("Nhâp chiều cao H là: "))
S_xq= 2*pi*r*h
S_tp= 2*pi*r*(r+h)
V= 2*pi*r*r*h
print(f"Diện tích xung quanh là: {S_xq:.2f}")
print(f"Diện tích toàn phần là: {S_tp:.2f}")
print(f"Thể tích là: {V:.2f}")