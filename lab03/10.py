n=int(input('nhập n: '))
a=2
while n>1:
    if n%a==0:
        print(a,end=' ')
        n//=a
    else:
        a+=1