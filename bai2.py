import random

def sinh_tap_tin_ngau_nhien(ten_tap_tin, so_luong, gia_tri_toi_da):
    """Sinh tệp tin với các số ngẫu nhiên."""
    cac_so = [random.randint(1, gia_tri_toi_da) for _ in range(so_luong)]
    with open(ten_tap_tin, 'w') as tap_tin:
        tap_tin.write(' '.join(map(str, cac_so)))

def doc_tap_tin_dau_vao(ten_tap_tin):
    """Đọc danh sách các số nguyên từ tệp tin."""
    with open(ten_tap_tin, 'r') as tap_tin:
        du_lieu = tap_tin.read().strip()
    cac_so = list(map(int, du_lieu.split()))
    return cac_so

def ghi_tap_tin_dau_ra(ten_tap_tin, cac_so):
    """Ghi danh sách các số nguyên vào tệp tin."""
    with open(ten_tap_tin, 'w') as tap_tin:
        tap_tin.write(' '.join(map(str, cac_so)))

def main():
    ten_tap_tin_dau_vao = 'lab11\package_2\Inp.txt'
    ten_tap_tin_dau_ra = 'lab11\package_2\out.dat'
    
    # Sinh tệp tin ngẫu nhiên với 10 số từ 1 đến 100
    sinh_tap_tin_ngau_nhien(ten_tap_tin_dau_vao, 10, 100)
    
    # Đọc các số từ tệp tin đầu vào
    cac_so = doc_tap_tin_dau_vao(ten_tap_tin_dau_vao)
    
    # Sắp xếp các số
    cac_so.sort()
    
    # Ghi các số đã sắp xếp vào tệp tin đầu ra
    ghi_tap_tin_dau_ra(ten_tap_tin_dau_ra, cac_so)

main()