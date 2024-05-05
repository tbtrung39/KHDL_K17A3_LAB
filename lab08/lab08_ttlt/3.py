def kiem_tra_so_nguyen_to(num):
    if num <2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num% i == 0:
            return False
    return True
def in_cac_so_nguyen_to(n):
    primes = []
    for i in range(2,n):
        if kiem_tra_so_nguyen_to(i):
            primes.append(i)
    return primes
n = int(input('Nhap n: '))
print(f'Cac so nguyen duong nho hon {n} la{in_cac_so_nguyen_to(n)}')            