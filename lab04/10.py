n=int(input("Nhập vào một số nguyên: "))
soNT=True
i=2
while i*i<=n:
    if(n%i==0):
        soNT=False
        break
    i+=1
if(soNT and n!=1):
    print(n," là số nguyên tố!")
else:
    print(n," không phải là số nguyên tố !!")
    
    
    
    
