def uoc_chung(a,b):
    a = []
    gcd =1
    while gcd <= min(a,b):
        if a% gcd == 0 and b% gcd ==0:
            a.append(gcd)
        gcd +=1
    return a
a = int(input('Nhap so thu nhat: '))
b = int(input("Nhap so thu hai: "))
all_uoc = uoc_chung(a,b)

print(f"Tat ca cac uoc chung cua {a} va {b} la:{all_uoc}")