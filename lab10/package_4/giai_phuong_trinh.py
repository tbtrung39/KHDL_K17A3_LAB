def phuong_trinh_bac_nhat(a,b):
    if a == 0:
        if b == 0:
            return "Phương trình có vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    else:
        return -b/a
    
def phuong_trinh_bac_hai(d,e,f):
    if d == 0:
        if e == 0:
            if f == 0:
                return "Phương trình có vô số nghiệm"
            else:
                return "Phương trình vô nghiệm"
        else:
            return -f/e
    else:
        delta = (e**2) - (4*d*f)
        if delta > 0:
            x1 = ((-e + delta)**0.5) / (2*d)
            x2 = ((-e - delta)**0.5) / (2*d)
            return f"Phương trình có hai nghiệm phân biệt x1 = {x1} và x2 = {x2}"
        elif delta == 0:
            x = -e / (2*d)  
            return f"Phương trình có nghiệm kép x = {x}"
        else:
            return "Phương trình vô nghiệm"  