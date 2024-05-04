def ucln(a,b):
    while b!=0:
        a,b = b, a%b
    return a
a = int(input('Nhập vào một số: '))
b = int(input('Nhập vào một số: '))
print(f'UCLN của {a} và {b} là: {ucln(a,b)}')