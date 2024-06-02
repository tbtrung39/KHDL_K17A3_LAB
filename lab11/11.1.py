def doc_so_tu_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines() 
    day_so = [int(so) for line in lines for so in line.split() if int(so) > 0]
    return day_so

def tinh_tong_so_le(day_so):
    tong = sum(so for so in day_so if so % 2 != 0)
    return tong

duong_dan_file = r'lab11\dayso.dat'

day_so = doc_so_tu_file(duong_dan_file)

tong_cac_so_le = tinh_tong_so_le(day_so)

print(f"tong cac so le la: {tong_cac_so_le}")