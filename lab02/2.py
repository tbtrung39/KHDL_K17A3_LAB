
a = float(input('nhap a: '))
b = float(input('nhap b: '))
c = float(input('nhap c: '))
delta = b**2-4*a*c
if delta >0:
    x1=(-b-delta**0.5)/2*a
    x2=(-b+delta**0.5)/2*a
    print(f'phuong trinh co 2 nghiem phan biet la: {x1},{x2}')
elif delta ==0:
    print(f'phuong trinh co 1 nghiem kep la:{-b/2*a}')
else:
    print('phuong trinh vo nghiem')
