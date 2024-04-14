ds=[int(x) for x in input('Nhập danh sách số nguyên, cách nhau bằng dấu cách: ').split()]
for i in ds:
    assert all (i%2==0 for i in ds)
print('Tất cả cá số trong danh sách đều là số chẵn')