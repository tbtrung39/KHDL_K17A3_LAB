n=int(input())
a=[]
c=2
while len(a)<n:
   for i in range(2,c):
       if c%i==0:
           break
   else:
       a.append(c)
   c+=1
print('A=',[i for i in a if n%i==0])
print('B=',[i for i in a if n%i!=0 and i<n])