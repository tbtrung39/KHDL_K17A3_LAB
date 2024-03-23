a = int(input("nhap a:"))
b = int(input("nhap b:"))
c = int(input("nhap c:"))
d = int(input("nhap d:"))
r = int(input("nhap r:"))
khoang_cach_im= ((a -c)**2 + (b-d)**2)**0.5
if khoang_cach_im > r :
    print("m nam ngoai duong tron:")
elif khoang_cach_im < r :
    print("m nam trong duong tron:")
else:
    print("m nam ngoai duong tron:")