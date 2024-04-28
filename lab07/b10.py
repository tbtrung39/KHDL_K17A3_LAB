m=int(input("Nhập số tự nhiên m: "))
n=int(input("Nhập số tự nhiên n: "))
m_str=str(m)
n_str=str(n)
chung=set()
for digit in m_str:
    if digit in n_str:
        chung.add(int(digit))
tong_chung=sum(chung)
print("Tổng các chữ số chung của m và n là: ", tong_chung)