sinh_vien = []
while True:
    ma_sv = input("Nhập mã sv: ")
    if ma_sv == '':
        break
    ho_ten = input("Nhập tên sv: ")
    diem_thi = float(input("Nhập điểm thi của sv: "))
    if diem_thi >10:
        break
    sinh_vien.append({
    "Mã SV": ma_sv,
    "Họ tên SV": ho_ten,
    "Điểm thi": diem_thi
})
print(sinh_vien)
