#viết chương trình sinh 1 dãy list A gồm 1000 số tự nhiên , nằm ngẫu nhiên trong khoảng[1,99999]
import random

danh_sach_A = []
for i in range(1000):
    so_ngau_nhien = random.randint(1, 99999)
    danh_sach_A.append(so_ngau_nhien)

print("Danh sách A:", danh_sach_A)
