tnct=float(input("Nhập vào TNCT: (tháng)"))
luong_cb=1350000
if tnct < 12 and tnct >= 0:
    he_so=2.34
if tnct >= 12 and tnct <= 36:
    he_so=3.33
if tnct >= 36 and tnct < 60:
    he_so=3.66
if tnct >= 60 :
    he_so = 3.99
luong=he_so*luong_cb
print(f"Lương của nhân viên là: {luong}")
