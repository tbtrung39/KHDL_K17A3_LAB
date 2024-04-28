from functools import reduce

def tong_va_danh_sach_so_chan(n):
    danh_sach = list(range(1, n + 1))
    so_chan = list(filter(lambda x: x % 2 == 0, danh_sach))
    tong = reduce(lambda x, y: x + y, so_chan) if so_chan else 0 
    return danh_sach, so_chan, tong

n = int(input("Nhập n: "))
danh_sach, so_chan, tong = tong_va_danh_sach_so_chan(n)

print("Danh sách các số từ 1 đến", n, "là:", danh_sach)
print("Danh sách các số chẵn từ 1 đến", n, "là:", so_chan)
print("Tổng các số chẵn từ 1 đến", n, "là:", tong)