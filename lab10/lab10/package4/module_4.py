def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    else:
        x = -b / a
        return f"Nghiệm của phương trình là x = {x}"

import math

def giai_phuong_trinh_bac_hai(a, b, c):
    if a <0:
        print('phương trình vô nghiệm')
    else:
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
        elif delta == 0:
            x = -b / (2*a)
            return f"Phương trình có nghiệm kép: x = {x}"
        else:
            return "Phương trình vô nghiệm trong tập số thực"

