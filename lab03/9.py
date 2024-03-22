# a
n = int(input("Nhập số nguyên n :"))
S4 = 0
for i in range(0,n + 1):
    if n <= 0 :
        break
    else:
        S4 += i ** 2
print(f"S4 : {S4}")
        
# b
n = int(input("Nhập số nguyên n :"))
S5 = 0
for i in range(0,n + 1):
    if n <= 0 :
        break
    else:
        S5 += (2 * i + 1) ** 3
print(f"S5 : {S5}")
        
# c
n = int(input("Nhập số nguyên n :"))
S6 = 0
for i in range(0,n + 1):
    if n <= 0 :
        break
    else:
        S6 += (2 * i) ** 4
print(f"S6 : {S6}")