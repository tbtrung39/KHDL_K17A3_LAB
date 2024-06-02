str1 = input('Nhập vào một chuỗi str1: ')
str2 = input('Nhập vào một chuỗi str2: ')
len1 = len(str1)
len2 = len(str2)
tron_str = ''

i = 0
j = 0
while i <len1 or j< len2:
    if i<len1:
        tron_str +=str1[i]
        i+=1
    if j <len2:
        tron_str +=str2[j]
        j+=1
print(f'Chuỗi sau khi trộn là: {tron_str}')