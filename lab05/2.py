n = input('nhap mot chuoi: ')
k = 0
for i in n:
    if not i.isalpha() and not i.isdigit():
        k+=1
print('so ki tu khong phai la so va chu tieng anh la',k)