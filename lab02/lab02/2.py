#ax^2+bx+c=0
import math
a=float(input("Nhập vào a:"))
b=float(input("Nhập vào b:"))
c=float(input("Nhập vào c:"))
delta=b**2 - 4*a*c 
if a == 0:
    x=-c/b
    print(f"Nghiệm của phương trình là : {x}")
elif delta == 0:
    x=-b/2*a
    print(f"Nghiệm của phương trình là {x}")
elif delta > 0:
    x1=(-b+math.sqrt(delta))/2*a
    x2=(-b+math.sqrt(delta))/2*a
    print(f"Nghiệm của phương trình là : {x1} và {x2}")
elif delta < 0:
    print(f"Nghiệm của phương trình là : {-b/2*a}+{math.sqrt(-delta)/2*a}i và {-b/2*a}-{math.sqrt(-delta)/2*a}i")
else:
    print("Sai")