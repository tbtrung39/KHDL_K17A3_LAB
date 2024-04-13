#1
n=int(input('nhập số lượng :'))
a=[]
b=[]
for i in range(n):
    tong = int(input())
    a.append(tong)
c= max (a)
for i in enumerate(n):
    if tong <c:
        b.append(tong)
max =max(b)
max_index=a.index(max)
print('phần tử lớn thứ hai của danh sách là',max)
print('phần tử lớn thứ hai của danh sách là',max_index)

#2
n=int(input(' nhập số lượng phần tử của danh sách:'))
a=[]

for i in range:
    num=int(input('nhập phần tử thứ {}:'.format(i +1)))
    a.append(num)
max_b=0
c=0
for num in a:
    if num>0:
        c+=1
        if c>max_b:
            max_b=c
        else:
            c=0
print('số lượng số dương liên tiếp nhiều nhất là:',max_b)

#3
n=int(input(' nhập số lượng phần tử của danh sách:'))
a=[]
for i in range(n):
    num=int(input(f'nhập phần tử thứ (i+1):'))
    a.append(num)
max = 0
b=0
c=0
for num in a:
    if num >0:
        b+=num
        c+=1
    else:
        if b>max:
            max = b
            k=c
if b>max:
    max = b
    k= c
print('số lượng các số dương liên tiếp với tổng lớn nhất là:',k)
