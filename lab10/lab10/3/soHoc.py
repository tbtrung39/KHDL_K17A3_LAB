def ucln(a,b):
    while b!=0:
        a,b = b, a%b
        return a
def bcnn(a,b):
    return (a*b)//ucln(a,b)