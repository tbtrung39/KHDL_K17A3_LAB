A = {1, 2, 3, 'abc', 11.9, "def", 9.4}
so_nguyen = 0
so_thuc = 0
chuoi_ki_tu = 0
for i in A:
    if isinstance(i, int):
        so_nguyen += 1
    elif isinstance(i, float):
        so_thuc += 1
    elif isinstance(i, str):
        chuoi_ki_tu += 1

print("Số phần tử là số nguyên trong tập hợp A:", so_nguyen)
print("Số phần tử là số thực trong tập hợp A:", so_thuc)
print("Số phần tử là chuỗi kí tự trong tập hợp A:", chuoi_ki_tu)