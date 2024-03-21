# viết chương trình nhập vào các hệ số a,b,c 
# in ra nghiệm của pt bậc 2 ax^2 + bx + c = 0
a = int(input("nhập a:"))
b = int(input("nhập b:"))
c = int(input("nhập c:"))
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b + delta**0.5)/2
    x2 = (-b - delta**0.5)/2
    print("phương trình có 2 nghiệm nphaan biệt")
elif delta == 0:
    print("phương trình có 1 nghiệm kép")
else:
    print("phương trình vô nghiệm")