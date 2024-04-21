sinh_vien = []
while True:
    ma_sv = input("Nhập mã sv: ")
    if ma_sv == '':
        break
    ho_ten = input("Tên sinh viên: ")
    diem_so = float(input("Điểm số của sv: "))
    if diem_so >10:
        break
    else:
        diem_so_2 = round(diem_so)
    sinh_vien.append({
        "Mã SV": ma_sv,
        "Họ tên SV": ho_ten,
        "Điểm số của SV": diem_so_2
    })

ds_diem_sv = []
for sv in sinh_vien:
    diem = sv["Điểm số của SV"]
    ds_diem_sv.append(diem)
    ds_diem_sv = sorted(ds_diem_sv,reverse= True)
print(ds_diem_sv)