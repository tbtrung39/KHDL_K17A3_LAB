# Đọc dữ liệu từ tập tin Sbd_Ph.dat
sbd_ph_data = {}
with open('Sbd_Ph.txt', 'r') as f:
    for line in f:
        sbd, phach = map(int, line.split())
        sbd_ph_data[sbd] = phach

# Đọc dữ liệu từ tập tin Sbd_Ten.txt
sbd_ten_data = {}
with open('Sbd_Ten.txt', 'r') as f:
    for line in f:
        sbd, ten = line.split(maxsplit=1)
        sbd_ten_data[int(sbd)] = ten.strip()

# Đọc dữ liệu từ tập tin Phieu_Diem.txt
phieu_diem_data = {}
with open('Phieu_Diem.txt', 'r') as f:
    for line in f:
        phach, diem = map(int, line.split())
        phieu_diem_data[phach] = diem

# Lắp ráp thông tin: Số báo danh, Họ tên và điểm thi của một thí sinh
thi_sinh = []
for sbd, phach in sbd_ph_data.items():
    if phach in phieu_diem_data:
        ten = sbd_ten_data.get(sbd, "Không có thông tin")
        diem = phieu_diem_data[phach]
        thi_sinh.append((sbd, ten, diem))

# Sắp xếp danh sách thí sinh theo điểm giảm dần
thi_sinh.sort(key=lambda x: x[2], reverse=True)

# Ghi dữ liệu ra tập tin Ketqua.txt
with open('Ketqua.txt', 'w') as f:
    for sbd, ten, diem in thi_sinh:
        f.write(f"{sbd}, {ten}, {diem}\n")
