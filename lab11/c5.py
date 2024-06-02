sbd_phach = {}
with open("Sbd_Ph.dat", "r") as file:
    for line in file:
        sbd, phach = map(int,line.strip().split())
        sbd_phach[sbd] = phach

sbd_ten = {}
with open("Sbd_Ten.txt", "r") as file:
    for line in file:
        sbd, ten = line.strip().split(maxsplit=1)
        sbd_ten[sbd] = ten

phach_diem = {}
with open("Phieu_Diem.txt", "r") as file:
    for line in file:
        phach, diem = line.strip().split()
        phach_diem[phach] = float(diem)

thong_tin = []
for sbd, phach in sbd_phach.items():
    if phach in phach_diem:
        diem = phach_diem[phach]
        if sbd in sbd_ten:
            ten = sbd_ten[sbd]
            thong_tin.append((sbd, ten, diem))

thong_tin.sort(key=lambda x: x[2], reverse=True)

with open("Ketqua.txt", "w") as file:
    for sbd, ten, diem in thong_tin:
        file.write(f"{sbd} ,{ten}, {diem}\n")


