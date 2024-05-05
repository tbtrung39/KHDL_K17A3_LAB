import math
r = float(input("Nhập bán kính hình tròn:"))
def tinh_chu_vi_hinh_tron(): # 2pir
    print(f"Chu vi hình tròn có bán kính r ={r} là:", 2*math.pi*r)
    return 

def tinh_dien_tich_hinh_tron():
    print(f"Diện tích của hình tròn có bán kính r ={r} là:", math.pi*r**2)
    return

tinh_chu_vi_hinh_tron()
tinh_dien_tich_hinh_tron()
