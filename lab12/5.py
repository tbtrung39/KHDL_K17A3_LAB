def S1(n):
    if n<1:
        return 0
    if n==1:
        return 1
    return n+S1(n-1)
def S2(n):
    if n<1:
        return 0
    if n==1:
        return 1
    return n**2 + S2(n-1)
while True:
    try:
        n=int(input('nhap n: '))
    except Exception as e:
        print(e)
        print('nhap lại')
    else:
        break
print('S1=',S1(n))
print('S2=',S2(n))