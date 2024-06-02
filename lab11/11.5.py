def doc_Sbd_Ph(duong_dan):
    with open(duong_dan, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    danh_sach = {}
    for line in lines:
        a, b = map(int, line.split())
        danh_sach[a] = b
    return danh_sach

def doc_Sbd_Ten(duong_dan):
    with open(duong_dan, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    danh_sach = {}
    for line in lines:
        a, ten = line.split(' st ')
        danh_sach[int(a)] = ten.strip()
    return danh_sach

def doc_Phieu_Diem(duong_dan):
    with open(duong_dan, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    danh_sach = {}
    for line in lines:
        a, diem = map(int, line.split())
        danh_sach[a] = diem
    return danh_sach

def ghi_ket_qua_vao_tap_tin(danh_sach, danh_sach_ten, duong_dan):
    with open(duong_dan, 'w', encoding='utf-8') as file:
        for sbd, diem in danh_sach:
            file.write(f"{sbd}, {danh_sach[sbd]}, {danh_sach_ten[sbd]}, {diem}\n")

duong_dan_Sbd_Ph = r"lab11\Sbd_Ph.txt"
duong_dan_Sbd_Ten = r"lab11\Sbd_Ten.txt"
duong_dan_Pheu_Diem = r"lab11\Phieu_Diem.txt"
duong_dan_ket_qua = r"lab11\ket_qua.txt"

danh_sach_Sbd_Ph = doc_Sbd_Ph(duong_dan_Sbd_Ph)
danh_sach_ten = doc_Sbd_Ten(duong_dan_Sbd_Ten)
danh_sach_Pheu_Diem = doc_Phieu_Diem(duong_dan_Pheu_Diem)

danh_sach_thi_sinh = [(sbd, danh_sach_ten[sbd], diem) for sbd, diem in danh_sach_Pheu_Diem.items() if sbd in danh_sach_Sbd_Ph.values()]

danh_sach_thi_sinh.sort(key=lambda x: x[2], reverse=True)

ghi_ket_qua_vao_tap_tin(danh_sach_thi_sinh, danh_sach_ten, duong_dan_ket_qua)