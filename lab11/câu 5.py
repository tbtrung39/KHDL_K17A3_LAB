sbd_phach = {}
with open('D:\\11_Nguyen_Minh_Hieu_0136\\KHDL_K17A3_LAB\\lab11\\Sbd_Ph.dat', 'r') as file:
    for line in file:
        sbd, phach = map(int, line.strip().split())
        sbd_phach[sbd] = phach
sbd_ten = {}
with open('D:\\11_Nguyen_Minh_Hieu_0136\\KHDL_K17A3_LAB\\lab11\\Sbd_Ten.txt', 'r') as file:
    for line in file:
        sbd, ten = line.strip().split(maxsplit=1)
        sbd_ten[int(sbd)] = ten
phach_diem = {}
with open('D:\\11_Nguyen_Minh_Hieu_0136\\KHDL_K17A3_LAB\\lab11\\Phieu_Diem.txt', 'r') as file:
    for line in file:
        phach, diem = map(int, line.strip().split())
        phach_diem[phach] = diem
sinh_vien = []
for sbd, phach in sbd_phach.items():
    ten = sbd_ten.get(sbd, 'Unknown')
    diem = phach_diem.get(phach, 0)
    sinh_vien.append((sbd, ten, diem))
sinh_vien.sort(key=lambda x: x[2], reverse=True)
with open('D:\\11_Nguyen_Minh_Hieu_0136\\KHDL_K17A3_LAB\\lab11\\Ketqua.txt', 'w') as file:
    for sbd, ten, diem in sinh_vien:
        file.write(f'{sbd} {ten} {diem}\n')

print('Kết quả đã được ghi vào tập tin Ketqua.txt.')