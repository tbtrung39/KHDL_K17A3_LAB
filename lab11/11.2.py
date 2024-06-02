def doc_tap_tin(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.read().strip().split('\n')  
    danh_sach = [int(so) for line in lines for so in line.split()]  
    return danh_sach

def ghi_tap_tin(danh_sach, path):
    with open(path, 'w', encoding='utf-8') as file:
        for so in sorted(danh_sach):  
            file.write(f"{so}\n")  

duong_dan_nhap = "lab11\Inp.txt"
duong_dan_xuat = "lab11\out.dat"

danh_sach = doc_tap_tin(duong_dan_nhap)

ghi_tap_tin(danh_sach, duong_dan_xuat)

with open(duong_dan_xuat, 'r', encoding='utf-8') as file:
    noi_dung = file.read()
print(noi_dung) 