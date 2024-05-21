Str1 = input("nhap chuoi: ")
Str2 = ''
for char in Str1:
    if char.isnumeric() == True:
        Str2 += char
print(Str2)
sum = 0
for i in range(1,int(Str2)):
    if int(Str2) % i !=0:
        continue
    elif int(Str2) % i ==0:
        sum += i
if sum == int(Str2):
    print(Str2, "la so hoan hao")
elif sum != int(Str2):
    print(Str2, "khong phai la so hoan hao")