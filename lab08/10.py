n=int(input('nhập n: '))
def uoc(n):
    a=[]
    for i in range(1,n):
        if n%i==0:
            a.append(i)
    return a
print(f'các ước của số {n} là: {uoc(n)}')