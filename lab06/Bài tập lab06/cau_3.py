danh_sach = []

while True:
    gia_tri = int(input("Nhập các giá trị là số tự nhiên: "))
    if gia_tri == 0:
        break
    danh_sach.append(gia_tri)
print("Danh sách các giá trị là: ", danh_sach)
# 
gia_tri_moi = int(input("Nhập vào giá trị mới: "))
vi_tri = int(input("Nhập vị trí muốn thêm vào (1 - đầu, 2 - cuối, 3 - thứ 5): "))
if vi_tri == 1:
    danh_sach.insert(0, gia_tri_moi)
elif vi_tri == 2:
    danh_sach.append(gia_tri_moi)
elif vi_tri == 3:
    danh_sach.insert(4, gia_tri_moi)
print("Danh sách sau khi thêm: ", danh_sach)
