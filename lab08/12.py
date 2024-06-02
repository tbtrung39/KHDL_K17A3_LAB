def nhap_thong_tin_nhan_vien():
    ho_ten = input("Nhập họ tên nhân viên: ")
    que_quan = input("Nhập quê quán của nhân viên: ")
    tham_niem = int(input("Nhập thâm niên công tác của nhân viên: "))
    return ho_ten, que_quan, tham_niem

def tinh_luong(tham_niem):
    if tham_niem >= 5:
        return 5000000
    elif tham_niem >= 3:
        return 4000000
    else:
        return 3000000

def xuat_thong_tin_nhan_vien(ho_ten, que_quan, tham_niem, luong):
    print(f"Họ tên: {ho_ten}")
    print(f"Quê quán: {que_quan}")
    print(f"Thâm niên công tác: {tham_niem} năm")
    print(f"Lương: {luong}")

def chuong_trinh_nhap_luong():
 ho_ten, que_quan, tham_niem = nhap_thong_tin_nhan_vien()
 luong = tinh_luong(tham_niem)
 xuat_thong_tin_nhan_vien(ho_ten, que_quan, tham_niem, luong)

chuong_trinh_nhap_luong()