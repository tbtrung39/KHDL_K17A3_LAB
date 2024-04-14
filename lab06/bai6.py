import random
A = []
for i in range(1000):
    so_ngau_nhien = random.randint(1,99999)
    A.append(so_ngau_nhien)
print("Danh sách ban đầu là:",A)    
#Sắp xếp tăng dần với sorted
sap_xep_1 = sorted(A)
print("Danh sách sau khi sắp xếp là:",sap_xep_1)
#Sắp xếp tăng dần không dùng sorted
# Sắp xếp tăng dần mà không dùng 'sorted' và không định nghĩa hàm
# Sử dụng thuật toán Bubble Sort trực tiếp trên list A

sap_xep_2 = A.copy()  # Tạo bản sao của list A để sắp xếp

n = len(sap_xep_2)
for i in range(n):
    for j in range(0, n-i-1):
        if sap_xep_2[j] > sap_xep_2[j+1]:
            sap_xep_2[j], sap_xep_2[j+1] = sap_xep_2[j+1], sap_xep_2[j]
print("Danh sách sau khi sắp xếp mà không dùng sorted là:",sap_xep_2)
