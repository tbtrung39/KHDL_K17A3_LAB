def is_TamGiac(a, b, c):
    "Kiem tra 3 canh a, b, c co tao thanh mot tam giac khong"
    return a+b>c and a+c>b and b+c>a 
def ChuviTamgiac(a, b, c):
    "Tinh chu vi tam giac voi 3 canh a, b, c"
    return a+b+c 
def S_TamGiac(a, b, c):
    "Tinh dien tich tam giac voi 3 canh a, b, c"
    s=(a*b*c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5

