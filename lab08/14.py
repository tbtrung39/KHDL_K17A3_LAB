# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử: "))

# Nhập danh sách số nguyên
numbers = []
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    numbers.append(num)

# Tính bình phương của từng số
square_numbers = list(map(lambda x: x**2, numbers))

# In danh sách bình phương
print("Danh sách bình phương:")
print(square_numbers)
