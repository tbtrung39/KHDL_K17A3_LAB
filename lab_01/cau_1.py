# câu 1: TÍNH SXQ , DIỆN TÍCH TOÀN PHẦN , THỂ TÍCH

import math
r = float(input("nhập giá trị:"))
h = float(input("nhập giá trị:"))
sxq = 2*3.14*r*h
dien_tich_tp= 2*3.14*r**2 + 2*3.14*r*h
the_tich = 3.14*(r**2)*h
print(f"diện tích xung quanh là:{sxq:.2f}")
print(f"diện tích toàn phần là:{dien_tich_tp:.2f}")
print(f"thể tích:{the_tich:.2f}")

