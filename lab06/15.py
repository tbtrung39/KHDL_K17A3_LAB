tuple = []
ten = input('Nhập tên người dùng: ')
tuoi = int(input('Nhập tuổi: '))
diem = int(input('Nhập điểm: '))
tuple.append((ten, tuoi, diem))
tuple.sort(key=lambda x: (x[0], x[1], x[2]))

print("Danh sách sau khi sắp xếp:")
for item in tuple:
    print(item)
