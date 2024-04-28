def tinh_luong(tham_nien):
    luong_co_ban=5000000
    if tham_nien < 5:
        phu_cap = 0
    elif tham_nien >=5 and tham_nien <= 10:
        phu_cap =10000000
    else:
        phu_cap =20000000
    luong=luong_co_ban+phu_cap
    return luong

def xuat_thong_tin(ho_ten,que_quan,tham_nien,luong):
    print("họ và tên: ", ho_ten)
    print("quê quán: ",que_quan)
    print("thâm niên: ", tham_nien)
    print("lương: ",luong)

def nhap_thong_tin():
    ho_ten = input("Nhập họ và tên: ")
    que_quan = input("Nhập quê quán: ")
    tham_nien = int(input("Nhập thâm niên: "))
    return ho_ten, que_quan, tham_nien

ho_ten, que_quan, tham_nien = nhap_thong_tin()
luong=tinh_luong(tham_nien)
xuat_thong_tin(ho_ten,que_quan,tham_nien,luong)