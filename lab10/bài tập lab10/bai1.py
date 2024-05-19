
a = int(input("Nhập độ dài cạnh a:"))
b = int(input("Nhập độ dài cạnh b:"))
c = int(input("Nhập độ dài cạnh c:"))

import hinhhoc.my_Triange as my_Triange 
print('Là tam giác:', end = " ")
print(my_Triange.is_TamGiac(a,b,c))

print('Chu vi của tang giác là:', end = " ")
print(my_Triange.ChuviTamGiac(a,b,c))

print('Diện tích của tam giác là:', end = " ")
print(my_Triange.S_TamGiac(a,b,c))