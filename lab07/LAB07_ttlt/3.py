import random
n = int(input("Nhap vao so luong phan tu cua tap hop A: "))
a = [random.uniform(-10,10)for _ in range(n) ]

min = min(a)
max = max(a)
sum_elments = sum(a)

print("Tap hop A: ", a)
print("Phan tu nho nhat: ",min)
print("Phan tu lon nhat: ",max)
print("Tong cac phan tu", sum_elments)
