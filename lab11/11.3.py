def doc_tap_tin(duong_dan):
    with open(duong_dan, 'r', encoding='utf-8') as file:
        lines = file.read().strip().split('\n')  
    danh_sach = [int(so) for line in lines for so in line.split()]  
    return danh_sach

def ghi_tap_tin(danh_sach, duong_dan):
    with open(duong_dan, 'w', encoding='utf-8') as file:
        for so in danh_sach:
            file.write(f"{so}\n") 

def tim_cuc_tri(danh_sach):
    cuc_tri = []
    for i in range(1, len(danh_sach) - 1):
        if (danh_sach[i - 1] < danh_sach[i] > danh_sach[i + 1]) or (danh_sach[i - 1] > danh_sach[i] < danh_sach[i + 1]):
            cuc_tri.append(danh_sach[i])
    return cuc_tri

duong_dan_nhap = r"lab11\f_in.dat"
duong_dan_xuat = r"lab11\f_out.dat"

danh_sach = doc_tap_tin(duong_dan_nhap)

cuc_tri = tim_cuc_tri(danh_sach)

with open(duong_dan_xuat, 'w', encoding='utf-8') as file:
    file.write(f"{len(cuc_tri)}\n")  
    for gia_tri in cuc_tri:
        file.write(f"{gia_tri} ")  