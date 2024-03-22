a = int(input("Nhap gia tri a"))
b = int(input("Nhap gia tri b"))
c = int(input("Nhap gia tri c"))
d = int(input("Nhap gia tri d"))
r = int(input("Nhap gia tri r"))
do_dai_IM = ((c-a)**2 + (d-b)**2)**0.5
if do_dai_IM > r:
    print("Diem M nam ngoai duong tron ")
if do_dai_IM == r:
    print("Diem M nam tren duong tron ")
else:
    print("Diem M nam trong duong tron ")