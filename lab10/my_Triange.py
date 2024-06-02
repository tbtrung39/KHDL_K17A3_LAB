import math
def is_tamgiac(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            return True
    return False

def chu_vi_tam_giac(a, b, c):
    if is_tamgiac(a, b, c):
        return a + b + c
    else:
        return None

def s_tam_giac(a, b, c):
    if is_tamgiac(a, b, c):
        p = chu_vi_tam_giac(a, b, c) / 2  # nửa chu vi
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return area
    else:
        return None

