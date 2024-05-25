import my_Triange
import mySquare
a = int(input('Nhập một cạnh của tam giác: '))
b = int(input('Nhập một cạnh của tam giác: '))
c = int(input('Nhập một cạnh của tam giác: '))
if my_Triange.tam_giac(a,b,c):
    print(f'Chu vi tam giác là: {my_Triange.chu_vi(a,b,c)}')
    print(f'Diện tích tam giác là: {my_Triange.dien_tich(a,b,c)}')
else:
    print('Các cạnh đã nhập không tạo thành tam giác.')
#
a = float(input('Nhập vào cạnh của hình vuông: '))
print(f'Chu vi hình vuông là: {mySquare.chu_vi_hinh_vuong(a)}')
print(f'Diện tích hình vuông là: {mySquare.dien_tich_hinh_vuong(a)}')
