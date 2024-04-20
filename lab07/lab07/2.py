numbers = []
while True: 
    n = input('Nhập vào một số tự nhiên(Nhấn enter để dừng): ')
    if n == '':
        break
    if n.isdigit():
        numbers.append(int(n))
    else:
        print('Vui lòng nhập số tự nhiên.')
a = set(numbers)

print(f'Danh sách Numbers: {numbers}')
print(f'Tập hợp A: {a}')