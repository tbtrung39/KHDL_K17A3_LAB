import random

n = int(input("Nhập số lượng phần tử: "))

A = set(random.random() for _ in range(n))

# Tìm phần tử lớn nhất, nhỏ nhất và tổng các phần tử trong A
max_value = max(A)
min_value = min(A)
sum_value = sum(A)

print("Tập hợp A:", A)
print("Phần tử lớn nhất trong A:", max_value)
print("Phần tử nhỏ nhất trong A:", min_value)
print("Tổng các phần tử trong A:", sum_value)