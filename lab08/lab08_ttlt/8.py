import math
def tinh_chu_vi(r):
    return 2* math.pi *r
def tinh_dien_tich(r):
    return math.pi * r **2
ban_kinh = float(input("Nhap ban kinh: "))
chu_vi = tinh_chu_vi(ban_kinh)
dien_tich = tinh_dien_tich(ban_kinh)
print(f"Chu vi hinh tron la: {chu_vi}")
print(f'Dien tich hinh tron la: {dien_tich}')
