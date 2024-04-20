import random
n = int(input('Nhập vào số lượng phần tử A: '))
a = [random.uniform(-10,10) for _ in range(n)]

min = min(a)
max = max(a)
sum_elements = sum(a)

print(f'Tập hợp A là: {a}')
print(f'Phần tử nhỏ nhất: {min}')
print(f'Phần tử lớn nhất: {max}')
print(f'Tổng các phần tử: {sum_elements}')