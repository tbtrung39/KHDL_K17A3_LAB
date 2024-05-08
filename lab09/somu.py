def somu(n,a):
    if n==0:
        return 1
    else:
        return a**n

a=int(input("Nhap so a can tim"))
n=int(input("Nhap luy thua can tim"))
print(somu(n,a))