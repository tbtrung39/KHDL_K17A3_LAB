#a
n = int(input("Nhập số nguyên n: "))
if n<=0:
    print("n phải là số nguyên dương")
else:
    tong = 0
    for i in range(1, n+1):
        tong += i
    print("Tổng ", n, "số nguyên dương đầu tiên là:", tong)


#b
n=int(input("Nhập số n: "))
if n<=0:
    print("n phải là số nguyên dương")
else:
    S2=0
    for i in range (1,n+1,2):
        S2+=i
    print("Tổng là",S2)

#c
n = int(input("Nhập số nguyên n: "))
if n<=0:
    print("n phải là số nguyên dương")
else:
    tong = 0
    for i in range(0,n+1,2):
        tong +=i
    print("Tổng=  ", tong)