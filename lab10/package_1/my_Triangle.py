import math
def is_TamGiac(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def ChuviTamGiac(a,b,c):
    P = a + b + c
    return P

def S_TamGiac(a,b,c):
    return math.sqrt((ChuviTamGiac(a,b,c) - a) * (ChuviTamGiac(a,b,c) - b) * (ChuviTamGiac(a,b,c) - c))