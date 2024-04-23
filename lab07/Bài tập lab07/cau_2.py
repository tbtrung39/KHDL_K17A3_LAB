n = int(input("Nhập số phần tử: "))
Numbers = []
for i in range(n):
    phan_tu = int(input("Nhập các giá trị: "))
    Numbers.append(phan_tu)
print(Numbers)
set_A = set(Numbers)
print(set_A)