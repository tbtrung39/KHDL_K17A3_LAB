
a=float(input('nhap gioi bat dau: '))
b= float(input('nhap gioi ket thuc:'))
if b<a:
    print('gioi bat dau phai nho hon gioi ket thuc')
gio_thue = b-a
if gio_thue<=3:
    gia_thue=gio_thue*100000
elif gio_thue>3:
    gia_thue=3*100000+(100000*0.75)*(gio_thue-3)
if a>=11 and a<15:
    if b>a and b<=15:
        gia_thue=gia_thue*0.9
print(f'so tien can phai tra la: {gia_thue} dong')
