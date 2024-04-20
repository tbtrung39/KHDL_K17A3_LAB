import random
digits = [str(i) for i in range(10)]
s = set(random.sample(digits,5))
print(f'Tập danh sách gồm 5 phần tử ngẫu nhiên là: {s}')