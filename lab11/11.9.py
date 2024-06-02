def doc_du_lieu(duong_dan):
    with open(duong_dan, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def tinh_tong_trong_luong(danh_sach_hanh_khach):
    tong_trong_luong = []
    for i in range(1, len(danh_sach_hanh_khach)):
        trong_luong = sum(map(int, danh_sach_hanh_khach[i].split()))
        tong_trong_luong.append(trong_luong)
    return tong_trong_luong

def kiem_tra_qua_gioi_han(danh_sach_trong_luong):
    qua_gioi_han = []
    for i in range(len(danh_sach_trong_luong)):
        if danh_sach_trong_luong[i] > 23:
            qua_gioi_han.append(i + 1)
    return qua_gioi_han

def kiem_tra_so_luong_hanh_ly(danh_sach_hanh_khach):
    vuot_qua_so_luong = []
    for i in range(1, len(danh_sach_hanh_khach)):
        so_luong = len(danh_sach_hanh_khach[i].split())
        if so_luong > 5:
            vuot_qua_so_luong.append(i + 1) 
    return vuot_qua_so_luong

duong_dan_passengers = r"lab11\PASSENGER.IN"

danh_sach_hanh_khach = doc_du_lieu(duong_dan_passengers)

tong_trong_luong = tinh_tong_trong_luong(danh_sach_hanh_khach)

qua_gioi_han = kiem_tra_qua_gioi_han(tong_trong_luong)

vuot_qua_so_luong = kiem_tra_so_luong_hanh_ly(danh_sach_hanh_khach)

with open(r"lab11\weight.out", 'w', encoding='utf-8') as file:
    for trong_luong in tong_trong_luong:
        file.write(f"{trong_luong}\n")

with open(r"lab11\CANCELED.OUT", 'w', encoding='utf-8') as file:
    for i in range(len(qua_gioi_han)):
        file.write(f"{qua_gioi_han[i]}\n")
    for i in range(len(vuot_qua_so_luong)):
        file.write(f"{vuot_qua_so_luong[i]}\n")