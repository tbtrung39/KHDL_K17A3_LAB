def nhap_thong_tin_sinh_vien():
    ho_ten = input("Nhập họ tên của sinh viên: ")
    diem_toan = float(input("Nhập điểm môn Toán: "))
    diem_ly = float(input("Nhập điểm môn Lý: "))
    diem_hoa = float(input("Nhập điểm môn Hóa: "))
    return ho_ten, diem_toan, diem_ly, diem_hoa

def tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa):
    diem_tb = (diem_toan + diem_ly + diem_hoa) / 3
    return diem_tb

def xuat_ket_qua(ho_ten, diem_tb):
    print(f"Họ tên sinh viên: {ho_ten}")
    print(f"Điểm trung bình: {diem_tb:.2f}")
ho_ten, diem_toan, diem_ly, diem_hoa = nhap_thong_tin_sinh_vien()
diem_tb = tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa)
xuat_ket_qua(ho_ten, diem_tb)
