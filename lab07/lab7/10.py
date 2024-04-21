m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

m_str = str(m)
n_str = str(n)


so_chung = set()


for digit in m_str:
    if digit in n_str:
        so_chung.add(int(digit))

tong_chu_so_chung = sum(so_chung)

print("Tổng các chữ số chung là: ", tong_chu_so_chung)