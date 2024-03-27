a = int(input("Nhap vao a:"))
b = int(input("Nhap vao b:"))
c = int(input("Nhap vao c:"))
d = int(input("Nhap vao d:"))
r = int(input("Nhap vao r:"))
#I(a,b)
#M(c,d)
#R = r
khoang_cach_IM = ((a-c)**2+ (b-d)**2)**0.5
if khoang_cach_IM > r:
    print("M nam ngoai duong tron")
elif khoang_cach_IM < r:
    print("M nam trong duong tron")
else:
    print("M nam tren duong tron")