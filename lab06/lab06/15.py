n = int(input("Nhập số lượng tuple: "))
danh_sach = []
for i in range(n):
    name = input("Nhập tên: ")
    age = int(input("Nhập tuổi: "))
    score = float(input("Nhập điểm: "))
    danh_sach.append((name, age, score))
danh_sach_sap_xep = sorted(danh_sach)
print("Danh sách sau khi sắp xếp:")
for item in danh_sach_sap_xep:
    print(item)
