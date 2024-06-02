#a,
n=int(input("Nhập n: "))
while n<=0:
    n=int(input("Yêu cầu nhập lại n: "))
S4=0
i=1
while i<=n:
    S4+=i**2
    i+=1
print(f"S4={S4}")


#b
n=int(input("Nhập n: "))
while n<=0:
    n=int(input("Yêu cầu nhập lại n: "))
S5=0
i=1
while i<=n:
    S5+=i**3
    i+=2
print(f"S5={S5}")

#c
n=int(input("Nhập n: "))
while n<=0:
    n=int(input("Yêu cầu nhập lại n: "))
S6=0
i=2
while i<=n:
    S6+=i**4
    i+=2
print(f"S6={S6}")

