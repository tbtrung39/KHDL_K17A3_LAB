import random
A = set()
B = set()
n = int(input("Nhập số lượng phần tử cho tập hợp A: "))
m = int(input("Nhập số lượng phần tử cho tập hợp B: "))
print("Nhập các phần tử cho tập hợp A:")
for _ in range(n):
    a = input("Nhập phần tử: ")
    A.add(a)
print("Nhập các phần tử cho tập hợp B:")
for _ in range(m):
    a = input("Nhập phần tử: ")
    B.add(a)
b = A.intersection(B)
print("Các phần tử chung của tập hợp A và B:", b)