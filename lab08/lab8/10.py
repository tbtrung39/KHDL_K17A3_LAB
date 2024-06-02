def a(n):
    c=[]
    for i in range(1,n+1):
        if n%i==0:
            c.append(i)
    if len(c)!=0:
        return c
    else:
        return 'không có số nào'
n=int(input('nhập:'))
print(a(n))
    