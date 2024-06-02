def r(n):
    if n<=0:
        print('bán kính phải lớn hơn 0')
    else:
        a=2*3.14*n
        b=3.14*n
        print(f'chu vi:{a}\n diện tích:{b}')
n=float(input('nhập bán kính:'))
r(n)