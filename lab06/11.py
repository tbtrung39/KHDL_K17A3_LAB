import random
n = int(input("Nhập số phần tử của danh sách A: "))
A = [int(input(f"Nhập phần tử thứ {i+1} của danh sách A: ")) for i in range(n)]
B = [num for num in A if num % 3 == 0 and num % 5 != 0]
print("Danh sách B:", B)
C = [num ** 2 for num in A]
print("Danh sách C:", C)
D = [random.choice([num for num in A if num % 3 == 0]) for _ in range(n // 2)] 
print("Danh sách D:", D)
