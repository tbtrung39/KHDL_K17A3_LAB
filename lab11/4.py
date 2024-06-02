def is_prime(n):
    """Kiểm tra số nguyên n có phải là số nguyên tố hay không."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(n):
    """Tìm các ước nguyên tố của số nguyên dương n."""
    factors = []
    # Kiểm tra ước từ 1 đến n
    for i in range(1, n + 1):
        if n % i == 0 and is_prime(i):
            factors.append(i)
    return factors
with open('lab11/f_in1.dat','r') as file:
    data = list(map(int,file.read().split()))
with open('lab11/f_out1.dat','w') as file:
    for i in data:
        for j in prime_factors(i):
            file.write(str(j)+' ')
        file.write('\n')

