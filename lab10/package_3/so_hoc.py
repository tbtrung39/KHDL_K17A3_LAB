import math
def ucln(a,b):
    while b != 0:
        a, b = b, a%b
    return a

def bcnn(a,b):
    return abs(a*b) // (ucln(a,b))  

def  sumDivisor(n):
    tong = 0
    uoc_so = []
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            uoc_so.append(i)
            if i != n // i:
                uoc_so.append(n // i)
    tong = sum(uoc_so)
    return uoc_so, tong