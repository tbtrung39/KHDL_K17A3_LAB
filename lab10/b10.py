from package import my_Triange as md
from package import my_square as ad
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
if md.is_Tam_Giac(a, b, c):
    print("Đây là tam giác hợp lệ")
    print(md.ChuviTamGiac(a, b, c), "là chu vi tam giác")
    print(md.S_TamGiac(a, b, c), "là diện tích tam giác")
else:
    print("Đây không phải là tam giác hợp lệ")
n = int(input("Nhập cạnh hình vuông: "))
print(ad.chuvihinhvuong(n), "là chu vi hình vuông")
print(ad.dientichhinhvuong(n), "là diện tích hình vuông")

