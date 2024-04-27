def nhap_thong_tin_sinh_vien():
    ho_ten=input("Nhập họ tên của sinh viên: ")
    diem_toan=float(input("Nhập điểm môn toán của sinh viên: "))
    diem_ly=float(input("Nhập điểm môn lý của sinh viên: "))
    diem_hoa=float(input("Nhập điểm môn hóa của sinh viên: "))
    return ho_ten, diem_toan, diem_ly, diem_hoa
def tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa):
    return (diem_toan+diem_ly+diem_hoa)/3
def xuat_ket_qua(ho_ten, diem_tb):
    print("Sinh viên", ho_ten, "có điểm trung bình là:", diem_tb)
ho_ten, diem_toan, diem_ly, diem_hoa=nhap_thong_tin_sinh_vien()
diem_tb=tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa)
xuat_ket_qua(ho_ten, diem_tb)