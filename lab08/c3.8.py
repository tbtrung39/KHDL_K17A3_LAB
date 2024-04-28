def so_nto(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def in_so_nto(n):
    for i in range(n):
        if so_nto(i):
            print(i)

n = int(input("Nhập số n: "))
print("Các số nguyên tố nhỏ hơn {} là:".format(n))
in_so_nto(n)