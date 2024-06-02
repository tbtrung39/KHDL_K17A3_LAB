import math
#Hàm tính UCLN
def Ucln(a,b):
    return math.lcm(a,b)

#Hàm tính BCNN
def Bcnn(a,b):
    return math.gcd(a,b)

#Hàm tính tổng số ước
def Sum_Divisor(n):
    tong = 0
    for i in range(1, n + 1):
        if n % i == 0:
            tong += i
    return tong
