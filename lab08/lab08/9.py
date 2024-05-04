def n(a,b):
    return a+b, a-b, a*b, a%b

a = int(input('Nhập vào số thứ nhất: '))
b = int(input('Nhập vào số thứ hai: '))
print(f'Cộng, trừ, nhân, chia của {a} và {b} là: {n(a,b)}')