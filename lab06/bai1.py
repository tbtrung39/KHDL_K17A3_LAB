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
print(value)
#Cau4
value1 = 0
for i in a:
    if a[i]<0:
        continue
    elif a[i]>0:
        if a[i]==len(a)-1:
         value1 =a[i]
         break
print(value1)

#Cau5
q = max(a)
solonnhat = a.index(q)+1
print(solonnhat,q)