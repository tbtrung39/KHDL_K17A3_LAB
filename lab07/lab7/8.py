import random
A=set()
for _ in range(10):
    loai=random.choice(["số nguyên", "số thực", "chuỗi ký tự"])
    if loai=="số nguyên":
        A.add(random.randint(1, 100))
    elif loai=="số thực":
        A.add(round(random.uniform(1,100), 2))
    else:
        A.add(''.join(random.choices('abcdefghijklmnopqrstuvxwxyz', k=random.randint(1,10))))
so_nguyen=0
so_thuc=0
so_chuoi=0
for phan_tu in A:
    if isinstance(phan_tu, int):
        so_nguyen+=1
    elif isinstance(phan_tu, float):
        so_thuc+=1
    else:
        so_chuoi+=1
print("Số phần tử là số nguyên trong tập hợp A:", so_nguyen)
print("Số phần tử là số thực trong tập hợp A:", so_thuc)
print("Số phần tử là chuỗi ký tự trong tập hợp A:", so_chuoi)