set1 = set()
n=int(input("Nhap so nguyen"))
for i in range(1,n+1):
 q=1/i
 set1.add(q)
p = sum(set1)
print(p)