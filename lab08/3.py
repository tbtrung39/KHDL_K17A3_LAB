def snt(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def csnt(n):
    a=[]
    for i in range(2,n):
        if snt(i):
            a.append(i)
    return a
n=int(input('nhập n:'))
print(f'các số nguyên dương nhỏ hơn {n} là {csnt(n)}')