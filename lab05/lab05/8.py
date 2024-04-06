str = 'Ngoc Huyen đz siu cấp vjp pro, đz nhấc zũ trụ'
n = input('Nhập vào từ đơn: ')
a = str.split()
count = 0
for i in a:
    if i == n:
        count += 1

print(f'Số lần xuất hiện từ đơn trong đoạn văn là: {count}')