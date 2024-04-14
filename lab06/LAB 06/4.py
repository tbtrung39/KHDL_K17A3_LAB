#cau a
h = [1,2,3]
a[0]= h[0]
a[-1]= h[1]
a[4]= h[2]
print('Danh sach tong sau khi thay the la:',a)
# cau b
b = int(input("Nhap vao phan tu can xoa: "))
for j in range(len(a)):
    if a[j]==b:
        for i in range(j,len(a)-1):
            a[j] = a[j+1]
            break
print("Truoc khi xoa",a)
a=a[:len(a)-1]
print("Sau khi xoa",a)
#cau c
for i in range(len(a)):
    for i in range(i+1,len(a)):
        if a[i] < a[j]:
            a[i],a[j] = a[j] , a[i]
print("Danh sach sau khi sap xep theo thu tu giam dan la: ", a)

#cau d
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print('Danh sach sau khi sap xep cac thu tu tang dan la:',a)

