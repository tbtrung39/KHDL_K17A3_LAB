def ucln(a,b):
    while b!=0:
        a,b = b, a%b
    return a
def bcnn(a,b):
    return (a*b)//ucln(a,b)
a = int(input('Nhập vào một số: '))
b = int(input('Nhập vào một số: '))
print(f'BCNNN của {a} và {b} là: {bcnn(a,b)}')