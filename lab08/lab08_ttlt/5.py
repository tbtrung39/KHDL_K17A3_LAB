def tim_ucln(a,b):
    while b != 0:
        a,b = b,a %b
        return a
a = int(input("Nhap so nguyen a: "))
b = int(input("Nhap so nguyen b: "))
ucln = tim_ucln(a,b)
print(f'Uoc chung lon nhat cua {a} va {b} la {ucln}')
    