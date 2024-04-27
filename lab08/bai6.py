def ucln(a, b):
    while b !=0:
        a, b = b, a%b
    return a
def bcnn(a, b):
    return(a*b)//ucln(a,b)
a = int(input("Nhập vào số a: "))
b = int(input("Nhập vào số b: "))
boi_chung = bcnn(a,b)
print("Bội chung nhỏ nhất của hai số",a,"và",b,"là:",boi_chung)