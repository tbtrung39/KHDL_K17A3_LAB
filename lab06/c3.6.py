danh_sach= []
while True :
    phan_tu = int(input(" nhap 1 so tu nhien (nhap 0 de key thuc): "))
    if phan_tu ==0:
        break 
    danh_sach.append(phan_tu)
print("danh sach ban dau :", danh_sach)

danh_sach_duong = [x for x in danh_sach if x >0]
danh_sach_am = [x for x in danh_sach if x <= 0]
danh_sach = danh_sach_duong + danh_sach_am
print("danh sach khi chuyen ac phan tu duong len dau :", danh_sach)

m = int(input("nhap so m: "))
danh_sach.insert(0, m)
danh_sach.append(m)
danh_sach.insert(4, m)
print(" danh sach sau khi tren so m: ", danh_sach)