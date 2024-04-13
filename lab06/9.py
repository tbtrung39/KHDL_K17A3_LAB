danh_sach=[int(x) for x in input("Nhập danh sách số nguyên, cách nhau bằng dấu cách: ").split()]
for num in danh_sach:
    assert all (num%2==0 for num in danh_sach)
print("Tất cả cá số trong danh sách đều là số chẵn")
