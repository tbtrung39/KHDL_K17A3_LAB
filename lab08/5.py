def tim_ucln(a, b):
    while b!=0:
        a, b=b, a%b 
    return a
a=int(input("Nhập số nguyên a: "))
b=int(input("Nhập số nguyên b: "))
ucln=tim_ucln(a, b)
print("UCLN của", a, "và", b, "là:", ucln)