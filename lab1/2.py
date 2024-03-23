import math
x=float(input("giá trị :"))
f=(-x+math.sqrt(x**2+4))/(x**4+1)**(1/7)
k_q=round(f,2)
print("kết quả =",k_q)