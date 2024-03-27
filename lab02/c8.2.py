luong_can_ban = 1350000
TNCT = int(input("Nhap tham nien cong tac cua nhan vien:"))
if TNCT < 12:
        he_so = 2.34
elif TNCT >= 12 and TNCT <36:
        he_so = 3.33
elif TNCT >= 36 and TNCT <60:
        he_so =3.66
else:
        he_so = 3.99
tinh_luong = he_so*luong_can_ban
print("Luong cua nhan vien la:",tinh_luong, "đồng")