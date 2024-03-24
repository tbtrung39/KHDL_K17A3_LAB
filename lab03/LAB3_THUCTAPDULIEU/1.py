n = int(input("Nhap so n: "))
tich =1
for i in range(1, n+1):
    tich *= (2*(i+1)/(2*i+3))
print (round(tich ,3))

        