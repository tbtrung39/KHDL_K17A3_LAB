import random 
import math

def tao_day_so(max_length = 100):
    length = random.randint(1, max_length)
    day_so = []
    for i in range (length):
        so_ngau_nhien = random.randint(1,100)
        day_so.append(so_ngau_nhien)
    return day_so

def kiem_tra_nguyen_to(n):
    if n <= 1:
        return False
    for i in range (2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def day_so_nguyen_to_chia_7(day_so):
    day_so_chia_7 = []
    for so in day_so:
        if kiem_tra_nguyen_to(so) and so % 7 == 0:
            day_so_chia_7.append(so)
    return day_so_chia_7 

def so_chinh_phuong(n):
    if n < 0:
        return False
    sqrt_n = math.isqrt(n)
    return sqrt_n * sqrt_n == n  

def day_so_chinh_phuong(day_so):
    day_so_chinh_phuong = []
    for so in day_so:
        if so_chinh_phuong(so):
            day_so_chinh_phuong.append(so)
    return day_so_chinh_phuong                    
        