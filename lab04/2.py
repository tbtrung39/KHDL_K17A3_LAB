n = int(input("Nhập vào số nguyên n: "))
s = 0
sb = 0
sc = 0
while n > 0:
    for i in range(1,n+1):
        if i % 2 == 0:
            s -= 1/i
        else:
            s += 1/i
    break
print(s)
while n > 0:
    for i in range(1,n):
        sb += 1/(i*(i+1))
    break
print(sb)
while n > 0:
    for i in range(2,n+1):
        sc += 1/(i**0.5)
    break
print(sc)