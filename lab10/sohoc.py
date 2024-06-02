def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def bcnn(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // ucln(a, b)

def sumdivisor(n):
    if n <= 0:
        return None
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += i
    return c

