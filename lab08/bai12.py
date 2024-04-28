def nhap_thong_tin_nhan_vien():
    ho_ten = input("Nhập họ và tên:")
    que_quan = input("Nhập quê quán:")
    tham_nien = int(input("Nhập thâm niên công tác:"))
    return ho_ten,que_quan,tham_nien
def tinh_luong(tham_nien):
    luong_can_ban = 50000000
    if tham_nien <5:
        phu_cap= 0
    elif tham_nien>5 and tham_nien<10:
        phu_cap= 1000000
    else:
        phu_cap=2000000
    luong = luong_can_ban+phu_cap
    return luong
def xuat_thong_tin_nhan_vien(ho_ten,que_quan,tham_nien,luong):
    print("Họ và tên: ", ho_ten)
    print("Quê quán:",que_quan)
    print("Thâm niên:",tham_nien)
    print("Lương:",luong,"VND")
    
ho_ten,que_quan,tham_nien,luong = nhap_thong_tin_nhan_vien()
luong= tinh_luong(tham_nien)
xuat_thong_tin_nhan_vien(ho_ten,que_quan,tham_nien,luong)