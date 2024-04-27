def tinh_diem_trung_binh(toan, ly, hoa):
    return (toan + ly + hoa) / 3

def in_ket_qua(ho_ten, diem_tb):
    print("Họ tên: ",ho_ten)
    print("Điểm trung bình: ",diem_tb)


ho_ten = input("Nhập họ tên của sinh viên: ")
diem_toan = float(input("Nhập điểm Toán của sinh viên: "))
diem_ly = float(input("Nhập điểm Lý của sinh viên: "))
diem_hoa = float(input("Nhập điểm Hóa của sinh viên: "))

diem_tb = tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa)
in_ket_qua(ho_ten, diem_tb)