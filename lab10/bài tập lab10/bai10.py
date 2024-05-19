a = int(input("Nhập độ dài cạnh a:"))
b = int(input("Nhập độ dài cạnh b:"))
c = int(input("Nhập độ dài cạnh c:"))

import hinhhoc.my_Triange as my_Triange 
print('Là tam giác:', end = " ")
print(my_Triange.is_TamGiac(a,b,c))