import math
import os

def la_so_nguyen_to(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def uoc_so_nguyen_to(n):
    cac_uoc = set()
    while n % 2 == 0:
        cac_uoc.add(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            cac_uoc.add(i)
            n //= i
    if n > 2:
        cac_uoc.add(n)
    return sorted(cac_uoc)

def doc_tap_tin_dau_vao(ten_tap_tin):
    with open(ten_tap_tin, 'r') as tap_tin:
        cac_so = [int(dong.strip()) for dong in tap_tin]
    return cac_so

def ghi_tap_tin_dau_ra(ten_tap_tin, du_lieu):
    with open(ten_tap_tin, 'w') as tap_tin:
        for dong in du_lieu:
            tap_tin.write(' '.join(map(str, dong)) + '\n')

def main():
    thu_muc = 'lab11/package_3'
    ten_tap_tin_dau_vao = os.path.join(thu_muc, 'f_in.dat')
    ten_tap_tin_dau_ra = os.path.join(thu_muc, 'f_out.dat')

    if not os.path.exists(ten_tap_tin_dau_vao):
        print(f"Tệp tin {ten_tap_tin_dau_vao} không tồn tại.")
        return
    
    cac_so = doc_tap_tin_dau_vao(ten_tap_tin_dau_vao)
    danh_sach_uoc_so_nguyen_to = [uoc_so_nguyen_to(so) for so in cac_so]
    ghi_tap_tin_dau_ra(ten_tap_tin_dau_ra, danh_sach_uoc_so_nguyen_to)

if __name__ == "__main__":
    main()