import math
#Hàm kiểm tra tam giác
def is_Tam_giac(a,b,c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False

#Hàm tính chu vi
def Chu_vi_Tam_Giac(a,b,c):
    return a+b+c

#Hàm tính diện tích tam giác
def S_TamGiac(a,b,c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


