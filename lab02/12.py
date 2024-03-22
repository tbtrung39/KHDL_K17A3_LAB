a=int(input("Nhap gia tri cua a: "))
b=int(input("Nhap gia tri cua b: "))
c=int(input("Nhap gia tri cua x: "))
d=int(input("Nhap gia tri cua y: "))
r=int(input("Nhap gia tri cua r: "))
do_dai_IM=((c-a)**2+(d-b)**2)**0.5
if do_dai_IM>r:
    print("Diem M nam ngoai duong tron")
elif do_dai_IM == r:
    print("Diem M nam tren duong tron")
else:
    print("Diem M nam ngoai duong tron")