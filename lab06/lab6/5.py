import random

danh_sach_A = []
for i in range(1000):
    so_ngau_nhien = random.randint(1, 99999)
    danh_sach_A.append(so_ngau_nhien)

print("Danh sách A:", danh_sach_A)