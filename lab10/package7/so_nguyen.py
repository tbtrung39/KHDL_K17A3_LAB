import random
import math
def sinh_day_so(so_luong=100, gioi_han=1000):
    "Sinh ngau nhien 1 day so nguyen"
    return [random.randint(1, gioi_han) for _ in range(so_luong)]
def la_so_nguyen_to(n):
    "Kiem tra so nguyen to"
    if n<2:
        return False
    for i in range (2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def liet_ke_nguyen_to_chia_het_cho_7(day_so):
    "Liet ke cac so nguyen to chia het cho 7"
    return [num for num in day_so if la_so_nguyen_to(num) and num%7==0]
def tinh_tong_so_le(day_so):
    "Tinh tong cac so le trong day so"
    return sum(num for num in day_so if num%2!=0)
def la_so_chinh_phuong(n):
    "Kiem tra so chinh phuong"
    can_bac_hai=int(math.sqrt(n))
    return can_bac_hai*can_bac_hai==n
def kiem_tra_va_hien_thi_so_chinh_phuong(day_so):
    "Kiem tra va hien thi cac so chinh phuong trong day"
    so_chinh_phuong=[num for num in day_so if la_so_chinh_phuong(num)]
    if so_chinh_phuong:
        return so_chinh_phuong
    else:
        return "Khong co so chinh phuong trong day"
