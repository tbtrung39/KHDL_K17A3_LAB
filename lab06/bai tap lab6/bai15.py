# Nhập danh sách các tuple từ người dùng
n = int(input("Nhập số lượng tuple: "))
tuple_ = []

for i in range(n):
    ten = input("Nhập tên: ")
    tuoi = int(input("Nhập tuổi: "))
    diem = float(input("Nhập điểm: "))
    tuple_.append((ten, tuoi, diem))

# Sắp xếp theo thứ tự: tên, tuổi, điểm
tuple_.sort(key=lambda x: (x[0], x[1], x[2]))

# In ra danh sách tuple đã sắp xếp
print("Danh sách tuple sau khi sắp xếp:")
for item in tuple_:
    print(item)
