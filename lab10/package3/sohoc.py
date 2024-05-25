def Ucln(a, b):
    "Tra ve uoc chung lon nhat cua 2 so nguyen a va b"
    while b!=0:
        a, b=b, a%b 
    return a 
def Bcnn (a, b):
    "Tra ve boi chung nho nhat cua 2 so nguyen a va b"
    return abs(a*b)//Ucln(a, b)
def SumDivisor(n):
    "Tra ve tong cac uoc cua n"
    tong=0
    for i in range(1, n+1):
        if n%i==0:
            tong+=i
    return tong

