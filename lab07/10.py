m = int(input('nhap vao 1 so m :'))
n = int(input('nhap vao 1 so n :'))
m_str = str(m)
n_str = str(n)
so_chung = set(m_str) & set(n_str)
tong = sum(int(a) for a in so_chung)
print(f'tong cac chu so chung cua {m} va {n} la : {tong}')