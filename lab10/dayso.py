import random
import math
def sinh_day_so(n=100, max_value=1000):
    day_so = [random.randint(1, max_value) for _ in range(n)]
    print(f"Dãy số ngẫu nhiên: {day_so}")
    return day_so
def so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def liet_ke_nguyen_to_chia_het_cho_7(day_so):
    ket_qua = [so for so in day_so if so_nguyen_to(so) and so % 7 == 0]
    print(f"Các số nguyên tố chia hết cho 7 trong dãy: {ket_qua}")
    return ket_qua
def tinh_tong_so_le(day_so):
    tong = sum(so for so in day_so if so % 2 != 0)
    print(f"Tổng các số lẻ trong dãy: {tong}")
    return tong
def so_chinh_phuong(n):
    can_bac_hai = int(math.sqrt(n))
    return can_bac_hai * can_bac_hai == n
def kiem_tra_so_chinh_phuong(day_so):
    ket_qua = [so for so in day_so if so_chinh_phuong(so)]
    if ket_qua:
        print(f"Các số chính phương trong dãy: {ket_qua}")
    else:
        print("Không có số chính phương trong dãy.")
    return ket_qua
