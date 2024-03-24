a= float(input("Nhập a là: "))
b= float(input("Nhập b là: "))
c= float(input("Nhập c là: "))
delta = b**2 - 4*a*c
if delta > 0:
    X1=(-b+delta**0.5)/(2*a)
    X2=(-b-delta**0.5)/(2*a)
    print(f"Nghiệm của phương trình là: {X1:.2f} và {X2:.2f}")
elif delta == 0:
    X= -b/2*a
    print(f"nghiệm kép của phương trình là: {X:.2f}")
else:
    print("PT vô nghiệm")