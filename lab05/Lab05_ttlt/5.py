str = input("Nhap chuoi ky tu: ")
a = ''.join(filter(str.isdigit, str))
print("Chuoi so sau khi loai bo cac ky tu khong phai la so: ",a)
b = int(a)
k = 0
for i in range(1, b):
    if b % i ==0:
        k +=1
if k == b:
    print("Day la day so hoan hao")
else:
    print('Day khong phai la day so khong hoan hao')            

