
def tim_bcnn(a,b):    
    def ucln(a,b):
        while(b):
            a,b = b, a % b
        return a
    return a * b // ucln(a,b)
 
a = int(input("nhap so a :"))
b = int(input("nhap so b :"))
bcnn = tim_bcnn(a,b)
print("boi chung nho nhat cua a va b la :",bcnn)    
