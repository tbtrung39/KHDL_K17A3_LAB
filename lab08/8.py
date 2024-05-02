
import math


def chu_vi(r):
    return r * math.pi * 2

def dien_tich(r):
    return r * r * math.pi

r = int(input("nhap ban kinh :"))
print("chu vi hinh tron :",chu_vi(r))
print("dien tich hinh tron :",dien_tich(r))
