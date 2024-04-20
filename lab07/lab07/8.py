a = set()
while True:
    element = input('Nhập các phần tử(enter để kết thúc): ')
    if element =='':
        break
    a.add(element)
so_nguyen = sum(n.isdigit() for n in a)
so_thuc = sum('.' in n and n.replace('.','',1).isgigit() for n in a)
str = len(a) -so_nguyen -so_thuc
print(f'Số lượng phần tử là số nguyên trong tập hợp là: {so_nguyen}')
print(f'Số lượng phần tử là số thực trong tập hợp: {so_thuc}')
print(f'Số lượng phần tử cuối chuỗi ký tự trong tập hợp là: {str} ')