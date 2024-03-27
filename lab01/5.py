a1 = int(input('Nhap vecto a1: '))
a2 = int(input('Nhap vecto a2: '))
a3 = int(input('Nhap vecto a3: '))
b1 = int(input('Nhap vecto b1: '))
b2 = int(input('Nhap vecto b2: '))
b3 = int(input('Nhap vecto b3: '))
tri_a = (a1**2 + a2**2 + a3**2)**0.5
tri_b = (b1**2 + b2**2 + b3**2)**0.5
cos_ab = a1*b1 + a2*b2 + a3*b3/((a1**2 + a2**2 + a3**2)**0.5)*((b1**2 + b2**2 + b3**2)**0.5)
tich_vo_huong = tri_a*tri_b*cos_ab
print(tich_vo_huong)