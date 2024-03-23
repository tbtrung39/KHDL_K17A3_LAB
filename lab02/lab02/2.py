a = float(input('Nhap vao so a: '))
b = float(input('Nhap vao so b: '))
c = float(input('Nhap vao so c: '))
delta = b**2 - 4*a*c
if delta < 0:
    print('Phuong trinh vo nghiem')
elif delta == 0:
    print('Phuong trinh co nghiem kiep')
    x1=x2= -b/(2*a)
    print(f' Nghiem cua phuong trinh la:{x1}')
else:
    print('Phuong trinh co hai nghiem phan biet:')
    x1=(-b + delta**0.5)/(2*a)
    x2=(-b - delta**0.5)/(2*a)
    print(f'Nghiem cua phuong trinh co x1 = {x1}')
    print(f'Nghiem cua phuong trinh co x1 = {x2}')