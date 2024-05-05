import random
a = set(input("Nhap vao cac phan tu cua tap hop A: ").split())
b = set(input("Nhap vao cac phan tu cua tap hop B: ").split())
intersction = a.intersection(b)
print(f"Cac phan tu cua A va B : {a},{b}")
