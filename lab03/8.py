n=int(input('nhap n: '))
if n<=0:
    print('nhap sai!')
else:
    s1=0
    s2=0
    s3=0
    for i in range(1,n+1):
        s1+=i
    for i in range(1,2*n+1,2):
        s2+=i
    for i in range(2,2*n+1,2):
        s3+=i
print(f's1={s1},s2={s2},s3={s3}')