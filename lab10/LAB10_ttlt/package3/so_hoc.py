def ucln(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return ucln(b % a,a)
def bnnn(a,b):
    return(a // ucln(a,b)) *b    