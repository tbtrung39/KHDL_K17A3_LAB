def nhap_thong_tin():
    ho_ten = input("Nhập họ và tên của sv: ")
    diem_Toan = float(input("Nhập điểm Toán của sv: "))
    diem_Ly = float(input("nhập điểm Lý của sv: "))
    diem_Hoa = float(input("nhập điểm Hoá của sv: "))
    return ho_ten, diem_Toan, diem_Ly, diem_Hoa

def xuat_thong_tin(ho_ten, diem_Toan, diem_Ly, diem_Hoa, diem_tb):
    print("họ và tên sinh viên: ", ho_ten)
    print("điểm Toán của sinh viên: ", diem_Toan)
    print("điểm Lý của sinh viên: ", diem_Ly)
    print("điểm Hoá của sinh viên: ", diem_Hoa)
    print(f"điểm tb của sinh viên: {diem_tb:.2f}")

def tinh_diem_tb(diem_Toan, diem_Ly, diem_Hoa):
    diem_tb = (diem_Toan + diem_Ly + diem_Hoa) / 3
    return diem_tb

ho_ten, diem_Toan, diem_Ly, diem_Hoa = nhap_thong_tin()
diem_tb = tinh_diem_tb(diem_Toan, diem_Ly, diem_Hoa)
xuat_thong_tin(ho_ten, diem_Toan, diem_Ly, diem_Hoa, diem_tb)