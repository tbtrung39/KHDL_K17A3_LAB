n = int(input('Nhập vào 1 giá trị: '))
so_hoan_hao = []

for i in range(2,n):
    s = 0
    for j in range(1,i):
        if i%j == 0:
            s += j
    if s == i:
        so_hoan_hao.append(i)
print(f'Các số hoàn hảo nhỏ hơn {n} là: {so_hoan_hao}')