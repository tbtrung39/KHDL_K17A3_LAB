a=int(input("Nhap so nguyen a: "))
b=int(input("Nhap so nguyen b: "))
if a<0 or b<0:
    print("a, b phai lon hon 0")
max=a
if max<b:
    max=b
while True:
    if max%a==0 and max%b==0:
        print(f"BCNN({a},{b})={max}")
        break
    max=max+1



