def tinh_diem_trung_binh():
    ho_ten = input("Nhập Họ và Tên:")
    Diem_Toan = float(input("Nhập điểm Toán:"))
    Diem_Li = float(input("Nhập điểm Lí:"))
    Diem_Hoa = float(input("Nhập điểm Hóa:"))
    diem_trung_binh = (Diem_Toan + Diem_Li + Diem_Hoa) / 3
    print(f"Điểm trung bình của {ho_ten} là:", diem_trung_binh)
    return diem_trung_binh

tinh_diem_trung_binh()
