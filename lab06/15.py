# Nhập số lượng tuple
n = int(input("Nhập số lượng tuple: "))

# Nhập các tuple
danh_sach = []
for i in range(n):
    ten = input("Nhập tên: ")
    tuoi = int(input("Nhập tuổi: "))
    diem = int(input("Nhập điểm: "))
    danh_sach.append((ten, tuoi, diem))

# Sắp xếp danh sách
danh_sach.sort(key = lambda x: (x[0], x[1], x[2]))

# In danh sách sau khi đã sắp xếp
for i in danh_sach:
    print(i)
