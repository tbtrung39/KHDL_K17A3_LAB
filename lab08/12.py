def nhap_thong_tin_nhan_vien():
    ho_ten = input("Nhập họ tên của nhân viên: ")
    que_quan = input("Nhập quê quán của nhân viên: ")
    nam_kinh_nghiem = int(input("Nhập số năm kinh nghiệm của nhân viên: "))
    return ho_ten, que_quan, nam_kinh_nghiem
def tinh_luong(nam_kinh_nghiem):
    luong_co_ban = 15000000 
    phu_cap = 2000000 * nam_kinh_nghiem  
    luong = luong_co_ban + phu_cap
    return luong
def xuat_thong_tin_nhan_vien(ho_ten, que_quan, nam_kinh_nghiem, luong):
    print("Thông tin nhân viên:")
    print(f"Họ tên: {ho_ten}")
    print(f"Quê quán: {que_quan}")
    print(f"Thâm niên công tác: {nam_kinh_nghiem} năm")
    print(f"Lương: {luong:,} VND")
ho_ten, que_quan, nam_kinh_nghiem = nhap_thong_tin_nhan_vien()
luong = tinh_luong(nam_kinh_nghiem)
xuat_thong_tin_nhan_vien(ho_ten, que_quan, nam_kinh_nghiem, luong)
