import math
x=float(input("Nhap x"))
f=math.log(4,x)+math.log(x,2)
if x>0 and x!=1:
    print(f"Gia tri bt la {f:.2f}")