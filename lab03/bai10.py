n=int(input('nhập n: '))
a=2
print("Phân tích thừa số nguyên tố của số",n,"là: ")
while n>1:
    if n%a==0:
        print(a,end=' ')
        n//=a
    else:
        a+=1