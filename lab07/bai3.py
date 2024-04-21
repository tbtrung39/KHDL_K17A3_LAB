import random
n = int(input('Nhập vào số lượng phần tử A: '))
a = [random.uniform(-10,10) for _ in range(n)]

min = min(a)
max = max(a)
tong_pt = sum(a)

print(f'Tập hợp A là: {a}')
print(f'Phần tử nhỏ nhất: {min}')
print(f'Phần tử lớn nhất: {max}')
print(f'Tổng các phần tử: {tong_pt}')