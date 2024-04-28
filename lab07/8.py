a = set()
while True:
    elm = input("nhap cac phan tu (enter de ket thuc) :")
    if elm == '':
        break
    a.add(elm)
so_nguyen = sum(n.isdigit() for n in a)
so_thuc = sum(',' in n and n.replace(',','',1).isdigit() for n in a)
str = len(a) - so_nguyen - so_thuc
print(f'so luong phan tu nguyen trong tap hop la :{so_nguyen}')
print(f'so luong phan tu cuoi trong chuoi ki tu trong tap hop : {so_thuc}')
    