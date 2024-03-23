n = int(input("Nhập số n: "))
s4 = 0
s5 = 0
s6 = 0
while n > 0:
    for i in  range(1,n+1):
        s4 += i**2
        if i % 2 != 0:
            s5 += i**3
        if i % 2 == 0:
            s6 += i**4
    break
print(f"S4 = {s4}")
print(f"S5 = {s5}")
print(f"S6 = {s6}")