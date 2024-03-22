import math
def tinh_thoi_gian_dung(v0):
    a = 1
    t = (5**(1/4) - v0**(1/4)) / math.log(5, 4)
    return round(t, 2)
v0 = float(input("Nhập vận tốc ban đầu của ô tô (m/s): "))
thoi_gian = tinh_thoi_gian_dung(v0)
print("Thời gian ô tô dừng khi người lái đạp phanh là:", thoi_gian, "giây")