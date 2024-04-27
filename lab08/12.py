
def nhap_thong_tin_nhan_vien():
    ho_ten=input ("Nhập họ và tên của nhân viên: ")
    que_quan=input ("Nhập quê quán của nhân viên: ")
    nam_tham_nien=int(input("Nhập số năm thâm niên công tác của nhân viên: "))
    return ho_ten, que_quan, nam_tham_nien 
def tinh_luong(nam_tham_nien) :
    luong_co_ban=10000000
    phu_cap=500000*nam_tham_nien 
    return luong_co_ban+phu_cap
def xuat_thong_tin_nhan_vien(ho_ten, que_quan, nam_tham_nien, luong) :
    print ("Họ và tên:", ho_ten)
    print ("Quê quán:", que_quan)
    print("Thâm niên công tác:", nam_tham_nien, "năm")
    print ("Lương", luong, "VNĐ")
ho_ten, que_quan, nam_tham_nien=nhap_thong_tin_nhan_vien()
luong=tinh_luong(nam_tham_nien)
xuat_thong_tin_nhan_vien(ho_ten, que_quan, nam_tham_nien, luong)