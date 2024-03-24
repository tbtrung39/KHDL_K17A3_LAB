
n=int(input('nhap n: '))
if n<=0:
    print('nhap sai!')
else:
    s4=0
    s5=0
    s6=0
    for i in range(1,n+1):
        s4+=i**2
    for i in range(1,2*n+1,2):
        s5+=i**3
    for i in range(2,2*n+1,2):
        s6+=i**4
print(f's4={s4},s5={s5},s6={s6}')
