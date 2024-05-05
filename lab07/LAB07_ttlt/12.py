import random as r
n=input('nhập chuỗi:')
dic={}
a=[]
for i in n:
   if a.count(i)==0:
       a.append(i)
for i in a:
    dic[f'{i}']=n.count(i)
print(dic) 
