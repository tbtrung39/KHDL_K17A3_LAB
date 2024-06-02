# Nhập số phần tử n và danh sách A từ bàn phím
n = int(input("Nhập số phần tử của danh sách A: "))
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]

# Sử dụng List Comprehension để thực hiện yêu cầu
# a. Tạo danh sách B chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5 từ danh sách ban đầu
B = [num for num in A if num % 3 == 0 and num % 5 != 0]
print("Danh sách B:", B)

# b. Tạo danh sách C với các phần tử là bình phương của danh sách A
C = [num**2 for num in A]
print("Danh sách C:", C)

# c. Tạo danh sách D gồm các phần tử lấy ngẫu nhiên từ danh sách A mà chia hết cho 3
import random
D = [num for num in random.sample(A, len(A)) if num % 3 == 0]
print("Danh sách D:", D)