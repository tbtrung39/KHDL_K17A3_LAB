Numbers = []
while True:
    n=input('nhập vào các chữ số tự nhiên (enter để dừng): ')
    if n=='':
        break
    if n.isdigit():
        Numbers.append(int(n))
    else:
        print('vui lòng nhập số tự nhiên!')
A=set(Numbers)
print(f'danh sách Numbers là: {Numbers}\n tập hợp A: {A}')