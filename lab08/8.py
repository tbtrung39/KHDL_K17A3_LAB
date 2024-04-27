import math
def tinh_chu_vi_ban_kinh(r):
    return 2*math.pi*r 
def tinh_dien_tich_ban_kinh(r):
    return 2*math.pi*(r**2)
ban_kinh=float(input("Nhập bán kính của hình tròn: "))
chu_vi=tinh_chu_vi_ban_kinh(ban_kinh)
dien_tich=tinh_dien_tich_ban_kinh(ban_kinh)
print("Chu vi hình tròn là: ", chu_vi)
print("Diện tích hình tròn là: ", dien_tich)