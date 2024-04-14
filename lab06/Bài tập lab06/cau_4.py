danh_sach = []
danh_sach_them = [1, 2, 3]

while True:
    phan_tu = int(input("Nhập các phần tử là số tự nhiên: "))
    if phan_tu == 0:
        break
    danh_sach.append(phan_tu)
# 
vi_tri = int(input("Nhập vị trí bạn muốn thêm vào(1 - đầu, 2 - cuối, 3 - thứ 5): "))
danh_sach_moi = []
if vi_tri == 1:
    danh_sach_moi = danh_sach_them + danh_sach
    print("Danh sách sau khi thêm: ", danh_sach_moi)
elif vi_tri == 2:
    danh_sach_moi = danh_sach + danh_sach_them
    print("Danh sách sau khi thêm: ", danh_sach)
elif vi_tri == 3:
    danh_sach_moi = danh_sach[:4] + danh_sach_them + danh_sach[4:]
    print("Danh sách sau khi thêm: ", danh_sach_moi)
# 
phan_tu_xoa = int(input("Nhập vị trí phần tử muốn xóa: "))
danh_sach_moi.pop(phan_tu_xoa)
print("Danh sách sau khi xóa là: ", danh_sach_moi)
# 
danh_sach_moi.sort()
print("Danh sách tăng dần: ", danh_sach_moi)
danh_sach_moi.sort(reverse = True)
print("Danh sách giảm dần: ", danh_sach_moi)
