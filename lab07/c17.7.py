sinh_vien = {}
n = int(input("Nhập số lượng sinh viên: "))
for i in range(n):
    ma_sv = input(f"Nhập mã sinh viên của sinh viên thứ {i+1}: ")
    ten_sv = input(f"Nhập tên sinh viên của sinh viên thứ {i+1}: ")
    while True:
        diem_sv = int(input(f"Nhập điểm số của sinh viên thứ {i+1} (0-10): "))
        if diem_sv in range(11):
            break
        else:
            print("Điểm số phải thuộc khoảng từ 0 đến 10.")
    sinh_vien[ma_sv] = {'Tên': ten_sv, 'Điểm': diem_sv}
sinh_vien_sap_xep = sorted(sinh_vien.items(), key=lambda x: x[1]['Điểm'], reverse=True)
print("\nDanh sách sinh viên theo điểm số giảm dần:")
for ma_sv, info in sinh_vien_sap_xep:
    print(f"Mã sinh viên: {ma_sv}, Tên sinh viên: {info['Tên']}, Điểm số: {info['Điểm']}")