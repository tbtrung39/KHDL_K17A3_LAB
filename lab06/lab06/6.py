import random
danh_sach = [random.randint(1, 99999) for _ in range(1000)]
print('danh sách ngẫu nhiên :',danh_sach)
danh_sach_sorted=sorted(danh_sach)
print('danh sách dùng sorted',danh_sach_sorted)
danh_sach_sort=danh_sach.sort
print('danh sách không dùng sorted',danh_sach_sort)