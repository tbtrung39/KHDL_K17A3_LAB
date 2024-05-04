def nguyen_to(n):
    if n<2:
        return False
    for i in range(2, n+1):
        if n%i == 0:
            return False
        else:
            return True

def nto_nho_hon_n(n):
    for i in range(2,n):
        if nguyen_to(i):
            print(i, end = ' ')
    print()

n = int(input('Nhập vào một giá trị: '))
nto_nho_hon_n(n)