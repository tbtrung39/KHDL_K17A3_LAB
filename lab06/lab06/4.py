danh_sach = []
while True:
    phan_tu = int(input("Nhập số tự nhiên (nhập 0 để kết thúc): "))
    if phan_tu == 0:
        break
    danh_sach.append(phan_tu)

print("Danh sách ban đầu:", danh_sach)
danh_sach_moi = danh_sach.copy()
danh_sach.insert(0, [1, 2, 3])  
danh_sach.insert(4, [1, 2, 3]) 
danh_sach.append([1,2,3])
print("Danh sách sau khi chèn [1,2,3]:", danh_sach)
k = int(input("Nhập vị trí phần tử cần xóa: "))
if k >= 0 and k < len(danh_sach):
    del danh_sach[k]
    print("Danh sách sau khi xóa phần tử thứ", k, ":", danh_sach)
else:
    print("Vị trí phần tử cần xóa không hợp lệ.")
danh_sach_moi.sort()
print("Danh sách sau khi sắp xếp tăng dần:", danh_sach_moi)
danh_sach_moi.sort(reverse=True)
print("Danh sách sau khi sắp xếp giảm dần:", danh_sach_moi)
