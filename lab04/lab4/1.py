n = int(input("nhập n: "))
while n<=0:
    print("Nhập lại n là số nguyên dương")
    n = int(input("nhâp n: "))

S4,S5,S6=0,0,0
i = 1
while i<=n:
    S4+=i**2
    S5+=(2*n+1)**3
    S6+=(2*n)**4
    i +=1

print(f"S4 = {S4}, S5 = {S5}, S6 = {S6}")
