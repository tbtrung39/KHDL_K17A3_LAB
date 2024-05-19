def Giaiphuongtrinhbacnhat(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình có vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    else:
        x = -b / a
        return x

import math
# ax^2 + bx + c = 0
def Giai_phuong_trinh_bac2(a, b, c):
    if a == 0:
        return "Đây không phải là phương trình bậc hai"
    
    delta = b ** 2 - 4 * a * c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return (x1, x2)
    elif delta == 0:
        x = -b / (2 * a)
        return (x)
    else:
        return "Phương trình vô nghiệm"
