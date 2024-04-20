n=int(input('nhập số tự :'))
a=0
so=2
while a<n:
    b=True
    for i in range(2,int(so**0.5)+1):
        if so%i==0:
            b=False
            break
    if b:
        print(so,end='')
        a+=1
    so+=1
