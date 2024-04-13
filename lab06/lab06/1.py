a=[2,-4,1,9,-3,6,3,-2,6,8]
s=0
for i in a:
    s+=i
print('tổng các phần tử trong danh sách:',s)
s_d=list(filter(lambda x:x>0,a))
t=0
for i in s_d:
    t=t+i
print('tổng các số dương là:',t)
a=[2,-4,1,9,-3,6,3,-2,6,8]
b= None
for i,c in enumerate(a):
    if c<0:
        b=i
        break
if b is not None:
    print('vị trí đầu tiên:',b)
else:
    print('không có vị trí đầu tiên')
b= None
for i in range(len(a)-1,-1,-1):
    if a[i]>0:
        b=i
        break
if b is not None:
    print('vị trí phần tử dương cuốI cùng:',b)
else:
    print('không có phần tử dương cuối cùng')

max = None
c= None
for i ,so in enumerate(a):
    if max is None or so >= max :
        max = so 
        c=i 
if c is not None:
    print('phần tử lớn nhất danh sách là',max)
    print('vị trí của phần tử lớn nhất cuối cùng là:',c)
else:
    print('danh sách trống')