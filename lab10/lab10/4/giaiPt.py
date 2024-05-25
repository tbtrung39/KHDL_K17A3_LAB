import math
def pt_bac_nhat(a,b):
    if a==0:
        if b==0:
            return 'Phương trình có vô số nghiệm'
        else:
            return 'Phương trình vô nghiệm'
    else:
        return -b/a
    
def pt_bac_hai(a,b,c):
    delta = b**2 - 4*a*c
    if delta <0:
        return 'Phương trình vô nghiệm'
    elif delta ==0:
        return -b/(2*a)
    else:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        return(x1,x2)
