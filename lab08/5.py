
def tim_ucln(a,b):
    while(b):
        a,b = b, a % b
        return a 
    
a = int(input("nhap so a :"))
b = int(input("nhap so b :"))
ucln = tim_ucln(a,b)
print("uoc chung lon nhat cua a va b la :",ucln)    
