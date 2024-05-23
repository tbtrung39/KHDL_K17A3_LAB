import random
import math

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def la_so_chinh_phuong(n):
    return math.isqrt(n)**2 == n

def sinh_day_so():
    day_so = [random.randint(1, 100) for _ in range(100)]
    print("Dãy số:", day_so)

    so_nguyen_to_chia_7 = [n for n in day_so if n % 7 == 0 and la_so_nguyen_to(n)]
    print("Các số nguyên tố chia hết cho 7:", so_nguyen_to_chia_7)


    tong_so_le = sum(n for n in day_so if n % 2 != 0)
    print("Tổng các số lẻ:", tong_so_le)

    so_chinh_phuong = [n for n in day_so if la_so_chinh_phuong(n)]
    if so_chinh_phuong:
        print("Các số chính phương:", so_chinh_phuong)
    else:
        print("Không có số chính phương trong dãy")

sinh_day_so()
