def doc_du_lieu_sbd_ph(filename):
    sbd_ph = {}
    with open(filename, 'r') as file:
        for line in file:
            sbd, ph = map(int, line.strip().split())
            sbd_ph[sbd] = ph
    return sbd_ph

def doc_du_lieu_sbd_ten(filename):
    sbd_ten = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            sbd = int(parts[0])
            ten = ' '.join(parts[1:])
            sbd_ten[sbd] = ten
    return sbd_ten

def doc_du_lieu_phieu_diem(filename):
    phieu_diem = {}
    with open(filename, 'r') as file:
        for line in file:
            ph, diem = map(float, line.strip().split())
            phieu_diem[ph] = diem
    return phieu_diem

def ghep_thong_tin(sbd_ph, sbd_ten, phieu_diem):
    danh_sach = []
    for sbd, ph in sbd_ph.items():
        if sbd in sbd_ten and ph in phieu_diem:
            ten = sbd_ten[sbd]
            diem = phieu_diem[ph]
            danh_sach.append((sbd, ten, diem))
    return danh_sach

def sap_xep_theo_diem(danh_sach):
    return sorted(danh_sach, key=lambda x: x[2], reverse=True)

def ghi_ket_qua(filename, danh_sach):
    with open(filename, 'w') as file:
        for sbd, ten, diem in danh_sach:
            file.write(f"{sbd} {ten} {diem}\n")

def main():
    sbd_ph_file = 'lab11/package_5/sbd_ph.dat'
    sbd_ten_file = 'lab11/package_5/sbd_ten.txt'
    phieu_diem_file = 'lab11/package_5/phieu_diem.txt'
    ket_qua_file = 'lab11/package_5/Ketqua.txt'

    
    sbd_ph = doc_du_lieu_sbd_ph(sbd_ph_file)
    sbd_ten = doc_du_lieu_sbd_ten(sbd_ten_file)
    phieu_diem = doc_du_lieu_phieu_diem(phieu_diem_file)
    danh_sach = ghep_thong_tin(sbd_ph, sbd_ten, phieu_diem)
    danh_sach = sap_xep_theo_diem(danh_sach)
    ghi_ket_qua(ket_qua_file, danh_sach)

main()