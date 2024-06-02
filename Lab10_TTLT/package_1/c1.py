a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh huyền c: "))
import my_Triangle 
print(my_Triangle.is_TamGiac(a,b,c))
print(my_Triangle.ChuviTamGiac(a,b,c), "là chu vi tam giác")
print(my_Triangle.S_TamGiac(a,b,c), "là diện tích tam giác")
