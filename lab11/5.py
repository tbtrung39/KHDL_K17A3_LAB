def read_sbd_ph(file_name):
    sbd_ph = {}
    with open(file_name, 'r') as file:
        for line in file:
            sbd, ph = map(int, line.split())
            sbd_ph[sbd] = ph
    return sbd_ph
def read_sbd_ten(file_name):
    sbd_ten = {}
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.split()
            sbd = int(parts[0])
            ten = ' '.join(parts[1:])
            sbd_ten[sbd] = ten
    return sbd_ten
def read_phieu_diem(file_name):
    phieu_diem = {}
    with open(file_name, 'r') as file:
        for line in file:
            ph, diem = map(int, line.split())
            phieu_diem[ph] = diem
    return phieu_diem
sbd_ph = read_sbd_ph('Sbd_Ph.dat')
sbd_ten = read_sbd_ten('Sbd_Ten.txt')
phieu_diem = read_phieu_diem('Phieu_Diem.txt')
thi_sinh_list = []
for sbd, ph in sbd_ph.items():
    if sbd in sbd_ten and ph in phieu_diem:
        ten = sbd_ten[sbd]
        diem = phieu_diem[ph]
        thi_sinh_list.append((sbd, ten, diem))
thi_sinh_list.sort(key=lambda x: x[2], reverse=True)
with open('Ketqua.txt', 'w') as file:
    for sbd, ten, diem in thi_sinh_list:
        file.write(f'{sbd} {ten} {diem}\n')
