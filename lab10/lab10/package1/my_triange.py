def tam_giac(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True
    elif a-b<c and b-c<a and c-a<b:
        return True
    else:
        return False

def chu_vi_tg(a,b,c):
    c_v=a+b+c
    return c_v

def s_tg(a,b,c):
    p=(a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**(1/2)
    return s
 