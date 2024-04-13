x = int(input("nhap x: "))
y = int(input("nhap y: "))
danh_sach_c = []
for i in range(0,x):
    danh_sach_s = []
    for j in range(0,y):
        kq = i*j
        danh_sach_s.append(kq)
    danh_sach_c.append(danh_sach_s)
print(danh_sach_c)