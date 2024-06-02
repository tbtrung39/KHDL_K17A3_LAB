import my_square
import my_Triangle
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
print(my_Triangle.is_TamGiac(a,b,c))
print(my_Triangle.ChuviTamGiac(a,b,c), "là chu vi tam giác")
print(my_Triangle.S_TamGiac(a,b,c), "là diện tích tam giác")

n = int(input("Nhập cạnh hình vuông: "))
print(my_square.chuviHinhVuong(n), "là chu vi hình vuông")
print(my_square.dien_tich_hinh_vuong(n), "là diện tích hình vuông")