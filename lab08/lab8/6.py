def d(a,b):
    c=a*b
    for i in range(1,c+1):
        if i%a==i%b==0:
            return i
a=int(input('nhập số a:'))
b=int(input('nhập số b:'))
print('BCNN=',d(a,b))
        