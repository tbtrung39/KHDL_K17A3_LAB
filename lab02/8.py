n=float(input("Nhap tham nien cong tac: "))
if n<12:
    he_so=2.34
elif n>=12 and n<36:
    he_so=3.33
elif n>=36 and n<60:
    he_so=3.66
elif n>=60:
    he_so=3.99
luong_can_ban=1350000
luong=he_so*luong_can_ban
print(f"Luong cua nhan vien la: luong={luong}")