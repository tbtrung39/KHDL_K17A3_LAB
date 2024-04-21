import random
n = int(input("Nhập số phần tử của danh sách A: "))
danh_sach_A = [int(input(f"Nhập phần tử thứ {i + 1}: ")) for i in range(n)]
danh_sach_B = [num for num in danh_sach_A if num % 3 == 0 and num % 5 != 0]
print("Danh sách B:", danh_sach_B)
danh_sach_C = [num**2 for num in danh_sach_A]
print("Danh sách C:", danh_sach_C)
danh_sach_D = random.choices([num for num in danh_sach_A if num % 3 == 0])
print("Danh sách D:", danh_sach_D)
