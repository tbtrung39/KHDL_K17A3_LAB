danh_sach=[]
while True:
    phan_tu=int(input("Nhập số tự nhiên (nhập 0 để dừng): "))
    if phan_tu==0:
        break
    danh_sach.append(phan_tu)
danh_sach.insert(0, [1, 2, 3])
danh_sach.append([1, 2, 3])
danh_sach.insert(4, [1, 2, 3]) 
print("Danh sách sau khi chèn:", danh_sach)
k=int(input("Nhập vị trí phần tử cần xóa(k): "))
if k >= 0 and k < len(danh_sach):
    del danh_sach[k]
print("Danh sách sau khi xóa phần tử thứ", k, ":", danh_sach)
danh_sach_tang_dan=sorted(danh_sach)
danh_sach_giam_dan=sorted(danh_sach,reverse=True)
print("Danh sách sau khi sắp xếp tăng dần:", danh_sach_tang_dan)
print("Danh sách sau khi sắp xếp giảm dần:", danh_sach_giam_dan)
