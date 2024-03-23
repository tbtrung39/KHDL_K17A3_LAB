so = int(input("Nhap vao mot so:"))
hang_tram = ['', 'mot','hai','ba','bon','nam','sau','bay','tam','chin']
hang_chuc = ['', 'mot','hai muoi','ba ','bon','nam','sau','bay','tam','chin']
hang_don_vi = ['', 'mot','hai','ba','bon','nam','sau','bay','tam','chin']
tram = so //100
chuc = (so%100)//10
don_vi = so % 10
if tram == 0:
    print(f'{hang_chuc[tram]} muoi {hang_don_vi[don_vi]}')
elif tram and chuc == 0:
    print(hang_don_vi[don_vi])
elif chuc == 0:
    print(f'{hang_tram[tram]} le {hang_don_vi[don_vi]}')
elif don_vi == 0:
    print(f'{hang_tram[tram]} tram {hang_chuc[chuc]}')
else:
    print(f'{hang_tram[tram]} tram {hang_chuc[chuc]} muoi {hang_don_vi[don_vi]}')