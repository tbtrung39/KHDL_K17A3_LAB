n = int(input('Nhập vào 1 giá trị: '))

flag = True
if n <=1:
    flag = False
for i in range(2, int(n**0.5)+1):
    if n%i == 0:
        flag = False
        break

if flag:
    print(f'{n} là số nguyên tố')
else:
    duoi = None
    tren = None
    for j in range(n-1,1,-1):
        so_nto_thap_hon = True
        for k in range(2,int(j**0.5)+1):
            if j % k == 0:
                so_nto_thap_hon = False
                break
        if so_nto_thap_hon:
            duoi = j
            break
    
    for h in range(n+1, n*2):
        so_nto_cao_hon = True
        for k in range(2, int(h**0.5)+1):
            if h%k == 0 :
                so_nto_cao_hon = False
                break
        if so_nto_cao_hon:
            tren = h
            break
    
if duoi is None:
    print(f'Không có số nguyên tố nhỏ hơn {n}')
elif tren is None:
    print(f'Không có số nguyên tố cao hơn {n}')
elif abs(n-duoi) <= abs(n-tren):
    print(f'{n} không phải là số nguyên tố.')
    print(f'Số nguyên tố gần nhất với {n} là: {duoi}')
else:
    print(f'{n} không phải là số nguyên tố. ')
    print(f'Số nguyên tố gần nhất với {n} là: {tren}')