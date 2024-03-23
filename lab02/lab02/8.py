tnct = int(input("Nhap so thang cong tac:"))
luong_can_ban = 1350000
if 0<= tnct < 12: 
    he_so = 2.34
elif 12<= tnct <36:
    he_so = 3.33
elif tnct < 60:
    he_so = 3.66
elif tnct>=60:
    he_so = 3.99
else:
    print('Khong hop le')
luong = he_so*luong_can_ban
print(f' Luong cua nhan vien la: {luong}')