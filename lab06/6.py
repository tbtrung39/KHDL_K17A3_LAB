#viết chương trình sinh 1 dãy list A gồm 1000 số tự nhiên , nằm ngẫu nhiên trong khoảng[1,99999] .Sau đó sắp xếp theo thứ tự tăng dần bằng 2 cách .
#Sử dụng hàm sorted và không sử dụng hàm sorted
import random

danh_sach_A = []
for i in range(1000):
    so_ngau_nhien = random.randint(1, 99999)
    danh_sach_A.append(so_ngau_nhien)

print("Danh sách A:", sorted(danh_sach_A))

sap_xep_khong_sorted = danh_sach_A.copy()  
for i in range(len(sap_xep_khong_sorted)):
    for j in range(i + 1, len(sap_xep_khong_sorted)):
        if sap_xep_khong_sorted[i] > sap_xep_khong_sorted[j]:
            sap_xep_khong_sorted[i],sap_xep_khong_sorted[j] = sap_xep_khong_sorted[j],sap_xep_khong_sorted[i]
print('Danh sách ko sử dụng hàm sorted :', sap_xep_khong_sorted)