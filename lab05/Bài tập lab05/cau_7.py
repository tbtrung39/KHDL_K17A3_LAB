Str = input("Nhập đoạn văn bản: ")
tu_can_tim = input("Nhập từ đơn cần tìm: ")
ds_tu = Str.split()
dem = 0
for w in ds_tu:
    if w.lower() == tu_can_tim.lower():
        dem += 1
print(f"Số lượng từ '{tu_can_tim}' trong đoạn văn bản là: {dem}")
