#kiem tra a,b,c co tao thanh mot tam giac khong?
# tinh chu vi tam giac
# tinh dien tich tam giac
import math
def is_tam_giac(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
def chu_vi_tam_giac(a,b,c):
    if a + b > c and a + c > b and b + c > a: 
        return a + b + c
    else:
        return None
def dien_tich_tam_giac(a,b,c):
        return math.sqrt((chu_vi_tam_giac(a,b,c)-a)*(chu_vi_tam_giac(a,b,c)-b)*(chu_vi_tam_giac(a,b,c)-c))

