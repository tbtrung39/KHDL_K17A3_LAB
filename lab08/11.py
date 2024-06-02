def nhap_thong_tin():
    ho_ten = input("Nhập họ tên của sinh viên: ")
    diem_toan = float(input("Nhập điểm Toán: "))
    diem_ly = float(input("Nhập điểm Lý: "))
    diem_hoa = float(input("Nhập điểm Hóa: "))
    return ho_ten, diem_toan, diem_ly, diem_hoa
#Hàm tính điểm trung bình
def tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa):
    return (diem_toan + diem_ly + diem_hoa) / 3
#Hàm xuất kết quả
def xuat_két_qua(ho_ten, diem_trung_binh):
    print(f"Họ tên: {ho_ten}")
    print(f"Điểm trung bình: {diem_trung_binh}")
#Sử dụng hàm
ho_ten, diem_toan, diem_ly, diem_hoa = nhap_thong_tin()
diem_trung_binh = tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa)
xuat_két_qua(ho_ten, diem_trung_binh)