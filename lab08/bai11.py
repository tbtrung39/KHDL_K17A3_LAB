def nhap_thong_tin_sinh_vien():
    ho_ten = input("Nhập họ và tên:")
    diem_Toan = int(input("Nhập điểm Toán:"))
    diem_Ly = int(input("NHập điểm Lý:"))
    diem_Hoa = int(input("Nhập điểm Hóa:"))
    return ho_ten,diem_Toan,diem_Ly,diem_Hoa
def tinh_diem_trung_binh():
    diem_Toan = float(input("Nhập điểm Toán: "))
    diem_Ly = float(input("Nhập điểm Lý: "))
    diem_Hoa = float(input("Nhập điểm Hóa: "))
    diem_TB = (diem_Toan+diem_Ly+diem_Hoa)/3
    return diem_TB
def xuat_thong_tin_sinh_vien(ho_ten,diem_Toan,diem_Ly,diem_Hoa,diem_TB):
    print("Họ và tên: ", ho_ten)
    print("Điểm Toán:", diem_Toan)
    print("Điểm Lý:", diem_Ly)
    print("Điểm Hóa:", diem_Hoa)
    print("Điểm trung bình:", diem_TB)
ho_ten,diem_Toan,diem_Ly,diem_Hoa = nhap_thong_tin_sinh_vien()
diem_TB = tinh_diem_trung_binh()
xuat_thong_tin_sinh_vien(ho_ten,diem_Toan,diem_Ly,diem_Hoa,diem_TB)