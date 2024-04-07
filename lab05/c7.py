str1 = input("Nhập chuỗi: ")
str2 = ''
for char in str1:
    if char.isnumeric() == True:
        str2 += char
print(str2)
sum = 0
for i in range(1,int(str2)):
    if int(str2) % i !=0:
        continue
    elif int(str2) % i ==0:
        sum += i
if sum == int(str2):
    print(str2, "là số hoàn hảo")
elif sum != int(str2):
    print(str2, "không phải số hoàn hảo")