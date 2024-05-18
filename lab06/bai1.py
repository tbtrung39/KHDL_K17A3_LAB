#cau 1
a = [2,-4,1,9,-3,6,3,-2,6,8]
q = sum(a)
print(q)
#cau 2
count1=0
count2=0
for i in a:
    if i>0:
        count1+=1
    elif i<0:
        count2+=1
print("Cac so duong la",count1)
print("Cac so am la",count2)
#Cau 3 
value=0
for i in a:
    if a[i]<0:
        value = a[i]
        break
vitri = a.index(value)+1
print("Vi tri phan tu am dau tien la",vitri)
#Cau4
a = [2,-4,1,9,-3,6,3,-2,6,8]
for i in range(len(a)-1, -1, -1):
    if a[i] > 0:
        print("Phần tử dương cuối cùng là:", a[i])
        break
if i == -1:
    print("List không có phần tử dương nào")

#Cau5
q = max(a)
solonnhat = a.index(q)+1
print(solonnhat,q)