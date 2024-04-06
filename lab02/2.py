a = int(input("nhap vao a:"))
b = int(input("nhap vao b:"))
c = int(input("nhap vao c:"))
delta = b**2-4*a*c
if delta > 0:
    print("pt co 2 no pb")
elif delta == 0:
    print("pt co 1 no kep")
else:
    print("pt vn")