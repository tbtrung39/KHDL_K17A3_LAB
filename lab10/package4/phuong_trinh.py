def phuong_trinh_bac_nhat(a, b):
    "Giai phuong trinh bac nhat ax+b=0"
    if a==0:
        if b==0:
            return "Phuong trinh vo so nghiem"
        else:
            return "Phuong trinh vo nghiem"
    else:
        return -b/a
def phuong_trinh_bac_hai(a, b, c):
    "Giai phuong trinh bac hai ax^2+bx+c=0"
    if a==0:
        return phuong_trinh_bac_nhat(b, c)
    delta=b**2-4*a*c
    if delta < 0:
        return "Phuong trinh vo nghiem"
    elif delta==0:
        return "Phuong trinh co nghiem kep x1=x2={x}"
    else:
        x1=(-b+delta**0.5)/(2*a)
        x2=(-b-delta**0.5)/(2*a)
        return "Phuong trinh co 2 nghiem phan biet x1={x1}, x2={x2}"

