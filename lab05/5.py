n = input('nhap ki tu:')
a = ''.join(filter(str.isdigit, n))
print('chuoi ki tu so la ', a)
number = int(a)
so_hoan_hao = sum([i for i in range(1,number) if number % i ==0])

if so_hoan_hao == number:
    print(f'{number} la so hoan hao')
else:
    print(f'{number} khong phai la so hoan hao')