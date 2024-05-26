def is_Tam_Giac(a,b,c):
    if a+b>c and a+c>b and c+b>a:
        return True
    return False
def ChuviTamGiac(a,b,c):
    return a+b+c
def S_TamGiac(a,b,c):
    s= (a+b+c)/2
    dien_tich = (s* (s-a)* (s-b)* (s-c))**0.5
    return dien_tich