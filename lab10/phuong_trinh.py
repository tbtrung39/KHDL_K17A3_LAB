import cmath

def giai_pt_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            return 
        else:
            return 
    else:
        return -b / a

def giai_pt_bac_hai(a, b, c):
    if a == 0:
        return giai_pt_bac_nhat(b, c)
    
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + cmath.sqrt(delta)) / (2 * a)
        x2 = (-b - cmath.sqrt(delta)) / (2 * a)
        return (x1.real, x2.real)
    elif delta == 0:
        x = -b / (2 * a)
        return (x.real,)
    else:
        x1 = (-b + cmath.sqrt(delta)) / (2 * a)
        x2 = (-b - cmath.sqrt(delta)) / (2 * a)
        return (x1, x2)

