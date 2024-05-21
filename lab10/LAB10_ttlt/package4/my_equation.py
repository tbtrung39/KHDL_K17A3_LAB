def pt_bac_nhat_mot_an(a,b):
    if a == 0:
        print("Vui long nhap lai")
    else:
        return -b/a
import math
def pt_bac_hai(a,b,c):
    delta = b**2 -4*a*c
    if delta < 0:
        print("Phuong trinh vo nghiem") 
    elif delta == 0:
        return -b/(2*a)
    else:
        print("nghiem 1: ",(-b,math.sqrt(delta) / (2*a)))
        print("nghiem 2: ",(-b,-math.sqrt(delta) / (2*a)))

