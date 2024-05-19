a = int(input("Nhập số a:"))
b = int(input("Nhập số b:"))

import sohoc
print(f'Ước chung lớn nhất của {a} và {b} là:', end = " ")
print(sohoc.Ucln(a,b))

print(f'Bội chung nhỏ nhất của {a} và {b} là:', end = " ")
print(sohoc.Bcnn(a,b))

n = int(input("Nhập số tự nhiên n:"))
print(f'Tổng các ước của {n} =', end = " ")
print(sohoc.sum_of_divisors(n))