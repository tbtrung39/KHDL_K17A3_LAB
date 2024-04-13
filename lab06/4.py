danh_sach = []
while True:
    so = int(input("Nhập số tự nhiên (nhập 0 để kết thúc): "))
    if so == 0:
        break
    danh_sach.append(so)
print("Danh sách ban đầu:", danh_sach)
danh_sach = [1, 2, 3] + danh_sach + [1, 2, 3]
print("Danh sách sau khi chèn vào đầu, cuối và thứ 5:", danh_sach)
k = int(input("Nhập vị trí k cần xóa trong danh sách: "))
if 0 <= k < len(danh_sach):
    del danh_sach[k]
    print("Danh sách sau khi xóa phần tử thứ k:", danh_sach)
else:
    print("Vị trí k không hợp lệ!")
danh_sach.sort()
print("Danh sách sau khi sắp xếp tăng dần:", danh_sach)
danh_sach.sort(reverse=True)
print("Danh sách sau khi sắp xếp giảm dần:", danh_sach)
