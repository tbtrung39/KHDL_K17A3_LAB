str1 = input("Nhap chuoi str1: ")
str2 = input("Nhap chuoi str2: ")
len1 = len(str1)
len2 = len(str2)
tron_str= ''
i=0
j=0
while i<len1 or j< len2:
    if i <len1:
        tron_str += str1[i]
        i+=1
    if j<len2:
        tron_str += str2[i]
        j+=1
print("Chuoi sau khi tron: ",tron_str)
