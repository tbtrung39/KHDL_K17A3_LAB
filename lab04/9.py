

n=int(input('nhap n: '))
for i in range(n,1,-1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        if i==n:
            print('n là số nguyên tố!')
        else:
            print('n không phải là số nguyên tố!')
        print('số nguyên tố nhỏ hơn hoặc bằng n nhất là',i)
        break
