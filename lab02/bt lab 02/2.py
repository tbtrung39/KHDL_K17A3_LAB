a=int(input("Nhập vào a: "))
b=int(input("Nhập vào b: "))
c=int(input("Nhập vào c: "))
delta=b**2-4*a*c
if delta >0:
    x1=(-b+(delta**0.5))/2*a
    x2=(-b-(delta**0.5))/2*a
    print("Phương trình có hai nghiệm phân biệt ")
    print("x1",x1 )
    print("x2",x2 )
elif delta ==0:
    x = -b / (2*a)
    print("Phương trình có một nghiệm kép:")
    print("x =", x)
else:
    print("Phương trình vô nghiệm")