danh_sach=[]
while True:
    phan_tu=int(input("Nhập một số tự nhiên(nhập 0 để kết thúc): "))
    if phan_tu==0:
        break
    danh_sach.append(phan_tu)
print("Danh sách ban đầu:", danh_sach)

danh_sach_duong=[x for x in danh_sach if x>0]
danh_sach_am=[x for x in danh_sach if x <= 0]
danh_sach=danh_sach_duong+danh_sach_am
print("Danh sách sau khi chuyển các phần tử dương lên đầu:", danh_sach)

m=int(input("Nhập số m: "))
danh_sach.insert(0, m)
danh_sach.append(m)
danh_sach.insert(4, m)
print("Danh sách sau khi chèn số m:", danh_sach)
