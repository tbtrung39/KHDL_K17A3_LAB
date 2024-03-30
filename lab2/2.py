a=int(input("nhập số a="))
b=int(input("nhập số b="))
c=int(input("nhập số c="))
delta=b**2-4*a*c
if delta <0:
    print("phương trình vô nghiệm")
elif delta==0:
    x=(-b)/(2*a)
    print(f"{x} là nghiệm kép của phương trình")
else:
    x1=(-b+(delta)**(1/2))/2*a
    x2=(-b-(delta)**(1/2))/2*a
    print(f"có hai nghiệm là {x1} và {x2}")