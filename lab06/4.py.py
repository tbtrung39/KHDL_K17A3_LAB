danh_sach = []
while True:
    n = int(input("nhập vào chuỗi một số nhập ở để kết thúc: ")) 
    if n == 0:
        break
    danh_sach.append(n)
print(f"danh sách sau khi kết thúc chương trình {danh_sach}")
m = [1,2,3]
danh_sach.append(m)
danh_sach.insert(0,m)
danh_sach.insert(4,m)
print(f"danh sách mới sau khi thêm {danh_sach}")

k = int(input("nhập vào vị trí của phần tử thứ k cần xóa: "))
danh_sach.remove(k)
print(f"danh sách sau khi xóa phần tử {k} là {danh_sach}")

danh_sach_moi = [i for i in danh_sach if i != [1,2,3]]
print(f"danh sách sắp xếp theo thứ tự tăng dần là {sorted(danh_sach_moi)}")
print(f"danh sách sắp xếp theo thứ tự giảm dần là {sorted(danh_sach_moi,reverse=True)}")