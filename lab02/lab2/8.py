TNCT = int(input("Nhập thân niên công tác của nhân viên (tháng) là: "))
luong= TNCT*1350000
if TNCT >0 and TNCT < 12:
    he_so =2.34
    print(f"Tiền lương nv là: {luong} đồng")
elif TNCT >=12 and TNCT <36:
    he_so= 3.33
    print(f"Tiền lương nv là: {luong} đồng")
elif TNCT >=36 and TNCT <60:
    he_so= 3.66
    print(f"Tiền lương nv là: {luong} đồng")
elif TNCT >=60:
    he_so= 3.99
    print(f"Tiền lương nv là: {luong} đồng")