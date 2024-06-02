from package import giaiphuongtrinh as vd
t=int(input('chon phuong trinh nuon giai: (1 or 2): '))
if t==1:
    print('ax+b=0')
    a=float(input('nhap a: '))
    b=float(input('nhap b: '))
    print(vd.phuong_trinh_bac1(a,b))
if t==2:
    print('ax^2 + bx + c = 0')
    a=float(input('nhap a: '))
    b=float(input('nhap b: '))
    c=float(input('nhap C: '))
    print(vd.phuong_trinh_bac2(a,b,c))