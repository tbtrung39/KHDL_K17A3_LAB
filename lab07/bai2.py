
n = int(input("Nhập số lượng phần tử của danh sách: "))

Numbers = []
for i in range(n):
    number = int(input("Nhập số tự nhiên thứ {}: ".format(i + 1)))
    Numbers.append(number)

set_A = set(Numbers)

print("Tập hợp A được tạo từ danh sách Numbers là:", set_A)
