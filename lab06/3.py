danh_sach = []
while True:
    so = int(input("Nhập số tự nhiên (nhập 0 để kết thúc): "))
    if so == 0:
        break
    danh_sach.append(so)
print("Danh sách ban đầu:", danh_sach)
danh_sach = [x for x in danh_sach if x > 0] + [x for x in danh_sach if x <= 0]
print("Danh sách sau khi chuyển các phần tử dương lên đầu:", danh_sach)
m = int(input("Nhập số m để chèn vào danh sách: "))
danh_sach.insert(0, m)  
danh_sach.append(m)    
danh_sach.insert(4, m)  
print("Danh sách sau khi chèn số m vào đầu, cuối và vị trí thứ 5:", danh_sach)
