import math
def tam_giac(a,b,c):
    return a+b>c and a+c>b and b+c >a
def chu_vi(a,b,c):
    return a+b+c
def dien_tich(a,b,c):
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))