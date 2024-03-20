chieu_cao = float(input('Nhap chieu cao: '))
ban_kinh = float(input('Nhap ban kinh: '))
pi = 3.14
S_xung_quanh = round(2 * pi * chieu_cao * ban_kinh, 2)
S_toan_phan = round(S_xung_quanh + (2 * pi * (ban_kinh**2)), 2)
the_tich = round(pi * (ban_kinh**2) * chieu_cao, 2)
print('Dien tich xung quanh: ', S_xung_quanh)
print('Dien tich toan phan: ', S_toan_phan)
print('The tich: ', the_tich)