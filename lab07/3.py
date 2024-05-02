
import random

A = []
n = int(input("nhap n :"))
A = set(random.uniform(0, 100000) for _ in range(n))
print("Tap hop A :")
min_A = min(A)
max_A = max(A)
sum_A = sum(A)
print("min_A :")
print("max_A :")
print("sum_A :")
