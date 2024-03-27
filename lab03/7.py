#a
n=int(input("Nhập n: "))
if n<=0:
    print("n phải là số nguyên dương")
else:
    S4=0
    for i in range(1,n+1):
        S4+=i**2
    print("Tổng S4=",S4)

#b
n=int(input("Nhập n: "))
if n<=0:
    print("n phải là số nguyên dương")
else:
    S5=0
    for i in range(1,n+1,2):
        S5+=i**3
    print("Tổng S5=",S5)

#c
n=int(input("Nhập n: "))
if n<=0:
    print("n phải là số nguyên dương")
else:
    S6=0
    for i in range(0,n+1,2):
        S6+=i**4
    print("Tổng S6=",S6)