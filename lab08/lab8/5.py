def c(a,b):
    m=max(a,b)
    for i in range(m,0,-1):
        if a%i==0 and b%i==0:
            return i
a=int(input('nhập a:'))
b=int(input('nhập b:'))
print('UCLN=',c(a,b))
