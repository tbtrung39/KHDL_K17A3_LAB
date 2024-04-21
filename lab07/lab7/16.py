a=[10,1,2,3,4,5,6]
dict={}
for i in range (len(a)):
    for j in range (i+1,len(a)):
        if a[i]+1==a[j]:
            dict[i]=j
print(dict)