n=int(input("Nhap so nguyen n: "))
if n<=0:
    print("Vui lòng nhập số nguyên dương lớn hơn 0")
tong=0
i=1
for i in range(1, n+1):
    tong+=i**2
    i+=1
print("Tong S4 = ", tong)

tong=0
i=1
for i in range(1, n+1):
    tong+=i**3
    i+=1
print("Tong S5 = ", tong)

tong=0
for i in range(1, n+1):
    tong+=(2*i)**4
print("Tong S6 = ", tong)