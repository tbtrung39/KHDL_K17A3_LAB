def ulcn(a,b):
    if b==0:
        return a
    return ulcn(b,a%b)
def bcnn(a,b):
    return int(a*b/ulcn(a,b))
def SumDivisor(n):
    a=sum([i for i in range(1, int(n/2)+1) if n%i==0])
    return a