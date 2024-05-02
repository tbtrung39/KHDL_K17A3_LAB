
# Khởi tạo danh sách
number = []

print("Nhập các số tự nhiên từ bàn phím (nhấn 'q' để kết thúc):")

while True:
    num = input()
    if num == 'q':  # Kết thúc khi người dùng nhập 'q'
        break
    number.append(int(num))

# Tạo tập hợp A từ danh sách number
A = set(number)

print("Tập hợp A sau khi nhập các số:", A)
