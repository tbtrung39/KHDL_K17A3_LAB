def tim_ucln(a, b):
    while(b):
        a, b = b, a % b
        return a


def rut_gon_phan_so(a, b):
        a = a // ucln
        b = b // ucln
        return a, b


a = int(input("nhap a :"))
b = int(input("nhap b :"))
ucln = tim_ucln(a,b) 
print("phan so rut gon la :",a, "/",b)   