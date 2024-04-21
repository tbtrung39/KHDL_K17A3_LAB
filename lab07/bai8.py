A = {1, 2, 3, 'lion', 2.4, "bear", 0.2}
so_nguyen = 0
so_thuc = 0
chuoi_ki_tu = 0
for item in A:
    if isinstance(item, int):
        so_nguyen += 1
    elif isinstance(item, float):
        so_thuc += 1
    elif isinstance(item, str):
        chuoi_ki_tu += 1

print("Số phần tử là số nguyên trong tập hợp A:", so_nguyen)
print("Số phần tử là số thực trong tập hợp A:", so_thuc)
print("Số phần tử là chuỗi kí tự trong tập hợp A:", chuoi_ki_tu)


