# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử: "))

# Nhập danh sách số nguyên
numbers = []
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    numbers.append(num)

# Tính bình phương của các số lẻ
odd_square_numbers = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers)))

# In danh sách bình phương các số lẻ
print("Danh sách bình phương các số lẻ:")
print(odd_square_numbers)
