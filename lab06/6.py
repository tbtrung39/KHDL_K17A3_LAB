import random

# Tạo list A gồm 1000 số tự nhiên ngẫu nhiên trong khoảng [1,99999]
A = [random.randint(1, 99999) for _ in range(1000)]

# Sắp xếp list A theo thứ tự tăng dần sử dụng hàm sorted()
A_sorted = sorted(A)
print("List A sau khi sắp xếp bằng hàm sorted():", A_sorted)

# Sắp xếp list A theo thứ tự tăng dần không sử dụng hàm sorted()
# Sử dụng thuật toán sắp xếp nổi bọt (bubble sort)
for i in range(len(A)):
    for j in range(len(A) - i - 1):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]

print("List A sau khi sắp xếp không sử dụng hàm sorted():", A)
