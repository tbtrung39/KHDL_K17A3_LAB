def is_TamGiac(a,b,c):
    if a != b !=c:
        return True
    return False

def ChuviTamGiac(a,b,c):
    return a + b + c

import math
def S_TamGiac(a,b,c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s