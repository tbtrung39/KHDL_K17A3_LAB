str = input("nhap chuoi ky tu ")
c = ''.join(filter(str.isdigit,str))
print("chuoi so sau khi bo cac ky tu khong phai la so",c)
b = int(c)
k = 0
for i in range (1,b):
    if k%1 == 0:
        k =+1
if k ==b :
    print(" day la so hoan hao ")
else:
    print("day khong phai so hoan hao")