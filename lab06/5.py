import random
a = []
for _ in range(1000):
    ngau_nhien = random.randint(1, 99999)
    a.append(ngau_nhien)
print("Danh sách A gồm 1000 số tự nhiên ngẫu nhiên trong khoảng từ 1 đến 99999:")
print(a)
