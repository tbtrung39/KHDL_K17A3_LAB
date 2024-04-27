from functools import reduce
def tinh_tong_so_chan(danh_sach):
    so_chan=filter(lambda x: x%2==0, danh_sach)
    return reduce(lambda x, y: x+y, so_chan, 0)
n=int(input("Nhập n: "))
danh_sach=[x for x in range(1, n+1)]
tong_so_chan=tinh_tong_so_chan(danh_sach)
print("Tổng các số chẵn từ 1 đến", n, "là:", tong_so_chan)