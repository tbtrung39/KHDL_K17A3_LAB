from functools import reduce
n = int(input("Nhập số n: "))
lst = list(range(1, n+1))
so_chan = filter(lambda x: x % 2 == 0, lst)
tong_so_chan= reduce(lambda x, y: x + y, so_chan)

print("Tổng các số chẵn từ 1 đến {}: {}".format(n, tong_so_chan))
