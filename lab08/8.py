import math
def tinh_chu_vi(r):
    return 2 * math.pi * r
def tinh_dien_tich(r):
    return math.pi * r ** 2
try:
    ban_kinh = float(input("Nhập bán kính của hình tròn: "))
    if ban_kinh <= 0:
        print("Bán kính phải là một số dương.")
    else:
        chu_vi = tinh_chu_vi(ban_kinh)
        dien_tich = tinh_dien_tich(ban_kinh)
        print(f"Chu vi của hình tròn là {chu_vi:.2f}")
        print(f"Diện tích của hình tròn là {dien_tich:.2f}")
except ValueError:
    print("Vui lòng nhập một số.")
