m = int(input('Nhập vào một số m: '))
n = int(input('Nhập vào một số n: '))

m_str=str(m)
n_str = str(n)

so_chung = set(m_str) & set(n_str)
tong = sum(int(a) for a in so_chung)
print(f'Tổng các số chung của {m} và {n} là: {tong}')