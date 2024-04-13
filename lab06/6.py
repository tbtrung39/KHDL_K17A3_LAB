import random
a = []
for _ in range(1000):
    random_num = random.randint(1, 99999)
    a.append(random_num)
print("Danh sách A trước khi sắp xếp:")
print(a)
n = sorted(a)
print("Danh sách A sau khi sắp xếp bằng hàm sorted():")
print(n)


n = len(a)
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print("Danh sách A sau khi sắp xếp không sử dụng hàm sorted():")
print(a)
