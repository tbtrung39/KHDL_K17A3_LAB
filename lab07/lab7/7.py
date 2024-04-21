import random
import string

# Nhập số lượng phần tử của tập hợp A và B
n = int(input("Nhập số lượng phần tử của tập hợp A: "))
m = int(input("Nhập số lượng phần tử của tập hợp B: "))

# Tạo tập hợp A và B với các ký tự ngẫu nhiên
A = set(random.choice(string.ascii_letters + string.digits) for _ in range(n))
B = set(random.choice(string.ascii_letters + string.digits) for _ in range(m))

print("Tập hợp A: ", A)
print("Tập hợp B: ", B)

# Tìm và in ra các phần tử chung của A và B
print("Các phần tử chung của A và B: ", A&B)