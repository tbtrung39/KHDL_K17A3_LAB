
a=float(input('nhap a:'))
b=float(input('nhap b:'))
c=float(input('nhap c:'))
d=float(input('nhap d:'))
r=float(input('nhap r:'))
kc=((c-a)**2+(d-b)**2)**0.5
if kc<r:
    print('diem m nam ben trong duong tron')
elif kc==r:
    print('diem m nam tren duong trong')
else:
    print('diem m nam ben ngoai duong tron')
