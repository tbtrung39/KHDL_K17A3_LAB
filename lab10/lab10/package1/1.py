import my_triange
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))
if my_triange.tam_giac(a,b,c):
    print('là tam giác')
else:
    print('không phải tam giác')
print(my_triange.chu_vi_tg(a,b,c),'là chu vi tam giác')
print(my_triange.s_tg(a,b,c), "là diện tích tam giác")