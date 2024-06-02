def doc_tap_tin(duong_dan):
    with open(duong_dan, 'r', encoding='utf-8') as file:
        lines = file.read().strip().split('\n') 
    danh_sach = [int(so) for so in lines]  
    return danh_sach

def kt_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_uoc_so_nguyen_to(n):
    uoc_so = []
    for i in range(1, n + 1):
        if n % i == 0 and kt_so_nguyen_to(i):
            uoc_so.append(i)
    return uoc_so

def ghi_tap_tin(danh_sach, duong_dan):
    with open(duong_dan, 'w', encoding='utf-8') as file:
        for so in danh_sach:
            uoc_so = tim_uoc_so_nguyen_to(so)  
            file.write(' '.join(map(str, uoc_so)) + '\n')  

duong_dan_nhap = r"lab11\f_in4.dat"
duong_dan_xuat = r"lab11\f_out4.dat"

danh_sach = doc_tap_tin(duong_dan_nhap)

ghi_tap_tin(danh_sach, duong_dan_xuat)

