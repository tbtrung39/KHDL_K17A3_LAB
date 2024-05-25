import myTriange
a = int(input('Nhập một cạnh của tam giác: '))
b = int(input('Nhập một cạnh của tam giác: '))
c = int(input('Nhập một cạnh của tam giác: '))
if myTriange.tam_giac(a,b,c):
    print(f'Chu vi tam giác là: {myTriange.chu_vi(a,b,c)}')
    print(f'Diện tích tam giác là: {myTriange.dien_tich(a,b,c)}')
else:
    print('Các cạnh đã nhập không tạo thành tam giác')