def s(x:int):
    if x<2:
        return False
    for j in range(2,x):
        if x%j==0:
            return False
    else:
        return True
n=int(input('nhập số:'))
a=[]
for i in range(0,n):
    if s(i):
        a.append(i)
if len(a)!=0:
    print(f'các số nguyên tố nhỏ hơn {n}: {a} ')
else:
    print('không có giá trị nào')