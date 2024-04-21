import random
import string

# Nhập số lượng phần tử của tập hợp A và B
n = int(input("Nhập số lượng phần tử của tập hợp A: "))
m = int(input("Nhập số lượng phần tử của tập hợp B: "))

# Tạo tập hợp A và B với các phần tử ngẫu nhiên
A = set(random.choice([random.randint(1, 100), random.uniform(1.0, 100.0), random.choice(string.ascii_letters)]) for _ in range(n))
B = set(random.choice([random.randint(1, 100), random.uniform(1.0, 100.0), random.choice(string.ascii_letters)]) for _ in range(m))

print("Tập hợp A: ", A)
print("Tập hợp B: ", B)

# Đếm số phần tử là số nguyên, số thực và chuỗi kí tự của tập hợp A
int_count = sum(isinstance(item, int) for item in A)
float_count = sum(isinstance(item, float) for item in A)
str_count = sum(isinstance(item, str) for item in A)

print("Số phần tử là số nguyên trong tập hợp A: ", int_count)
print("Số phần tử là số thực trong tập hợp A: ", float_count)
print("Số phần tử là chuỗi kí tự trong tập hợp A: ", str_count)