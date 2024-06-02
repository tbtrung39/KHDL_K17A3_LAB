# Đọc dữ liệu từ file input.txt
with open('input.txt', 'r') as f:
    data = f.readlines()

# a. Hiển thị nội dung dòng đầu tiên và dòng thứ 3
print("Dòng đầu tiên và dòng thứ ba:")
print(data[0].strip())
print(data[2].strip())

# b. Hiển thị nội dung toàn bộ file
print("\nNội dung toàn bộ file:")
for line in data:
    print(line.strip())

# c. Tìm và ghi các số lẻ vào file ODD.txt
odd_numbers = []
for line in data:
    numbers = line.split()
    for num in numbers:
        if int(num) % 2 != 0:
            odd_numbers.append(int(num))

# Thêm các số 0 vào odd_numbers nếu cần để tạo thành ma trận 4x4
while len(odd_numbers) < 16:
    odd_numbers.append(0)

# Chia odd_numbers thành các hàng của ma trận 4x4
odd_matrix = [odd_numbers[i:i+4] for i in range(0, len(odd_numbers), 4)]

# Ghi ma trận số lẻ vào file ODD.txt
with open('ODD.txt', 'w') as f:
    for row in odd_matrix:
        f.write(' '.join(map(str, row)) + '\n')

# d. In ra nội dung dòng cuối của file ODD.txt
with open('ODD.txt', 'r') as f:
    odd_data = f.readlines()

print("\nDòng cuối của file ODD.txt:")
print(odd_data[-1].strip())
