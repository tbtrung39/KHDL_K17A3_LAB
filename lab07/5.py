import random

# Tạo một danh sách gồm 10 chữ số từ 0 đến 9
numbers = list(range(10))

# Chọn ngẫu nhiên 5 phần tử từ danh sách numbers
A = set(random.sample(numbers, 5))

print("Tập hợp A gồm 5 phần tử ngẫu nhiên từ danh sách 10 chữ số từ 0 đến 9:", A)
