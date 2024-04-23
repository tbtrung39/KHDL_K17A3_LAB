m = int(input("Nhập một số thứ nhất: "))
n = int(input("Nhập một số thứ hai: "))
m_str = str(m)
n_str = str(n)
chu_so_m = set(m_str)
chu_so_n = set(n_str)
chu_so_chung = chu_so_m.intersection(chu_so_n)
tong = 0
for i in chu_so_chung:
    tong += int(i)
print(f"Tổng các chữ số chung của {m} và {n} là: {tong}")
