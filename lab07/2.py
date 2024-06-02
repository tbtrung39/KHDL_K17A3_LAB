Numbers = []

print("Nhập các số tự nhiên bạn muốn thêm vào danh sách. Nhập 'q' để kết thúc.")

while True:
    num = input()

    if num.lower() == 'q':
        break

    if num.isdigit():
        Numbers.append(int(num))

A = set(Numbers)

print("Tập hợp A:", A)
