n = int(input('Nhập 1 giá trị: '))

for i in range(2,n+1):
    nto = True
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            nto = False
            break
    if nto:
        print(f'Các số nguyên tố <= {n} là: {i}')