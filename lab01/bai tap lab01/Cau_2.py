h = float(input('Nhap chieu cao: '))
R = float(input('Nhap ban kinh: '))
pi = 3.14
S_xung_quanh = round(2 * pi * h * R, 2)
S_toan_phan = round(S_xung_quanh + (2 * pi * (R**2)), 2)
the_tich = round(pi * (R**2) * h, 2)
print('Dien tich xung quanh: ', S_xung_quanh)
print('Dien tich toan phan: ', S_toan_phan)
print('The tich: ', the_tich)