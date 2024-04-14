danh_sach = []
while True:
    so = int(input("Nhập vào một số(Kết thúc bằng số 0):"))
    danh_sach.append(so)
    if so == 0:
        break
print("Danh sách ban đầu là:",danh_sach)
#Chèn danh sách
danh_sach_copy_1 = danh_sach.copy()
danh_sach_copy_1.insert(0,[1,2,3])
danh_sach_copy_1.insert(5,[1,2,3])
danh_sach_copy_1.append([1,2,3])
print(danh_sach_copy_1)
danh_sach_copy_2 = danh_sach.copy()
k = int(input("Nhập vị trí cần xóa: "))
del danh_sach_copy_2[k]
print("Danh sách sau khi xóa phần tử thứ",k,"là:",danh_sach_copy_2)
danh_sach_copy_3 = danh_sach.copy()
sap_xep_tang_dan = sorted(danh_sach_copy_3)
print("Danh sách sắp xếp tăng dần là:",sap_xep_tang_dan)
sap_xep_giam_dan = sorted(danh_sach_copy_3) [::-1]
print("Danh sách sắp xếp giảm dần là:",sap_xep_giam_dan)
