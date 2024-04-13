danh_sach = []

print("Nhập các phần tử của danh sách (nhập 0 để kết thúc): ")
while True:
    phan_tu = int(input("Nhập phần tử: "))
    if phan_tu == 0:
        break
    danh_sach.append(phan_tu)

print("Danh sách ban đầu:", danh_sach)
i = 0
while i < len(danh_sach):
    if danh_sach[i] > 0:
        phan_tu_duong = danh_sach.pop(i)
        danh_sach.insert(0, phan_tu_duong)
    i += 1

print("Danh sách sau khi chuyển các phần tử dương lên đầu:", danh_sach)
m = int(input("Nhập số m để chèn vào danh sách: "))
danh_sach.insert(4, m)
danh_sach.insert(0, m)  
danh_sach.append(m)   
print("Danh sách sau khi chèn số m:", danh_sach)
