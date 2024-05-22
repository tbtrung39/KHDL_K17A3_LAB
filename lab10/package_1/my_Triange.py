def kiem_tra_tam_giac(a,b,c):
    return a + b > c and a + c >b and b + c > a

def chu_vi_tam_giac(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return a + b + c 
    else:
        return "Đây không phải tam giác"
    
def dien_tich_tam_giac(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        p = (a+b+c)/2
        return (p*(p-a)*(p-b)*(p-c))**(1/2)
    else:
        return "Đây không phải tam giác"