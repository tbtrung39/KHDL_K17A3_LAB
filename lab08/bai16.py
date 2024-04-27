def ds_so_chan():
    danh_sach = []
    for i in range (1, 101):
        if i % 2 == 0:
            danh_sach.append(i)
    return danh_sach
print(ds_so_chan())        