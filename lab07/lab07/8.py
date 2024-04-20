A = set()
n = int(input('Nhập số lượng phần tử của tập hợp A: '))
print('Nhập các phần tử của tập hợp A:')
for _ in range(n):
    a = input('Nhập phần tử: ')
    A.add(a)
b = 0
c = 0
d = 0

for k in A:
    if k.isdigit():
        b += 1
    elif '.' in k and all(part.replace('.', '').isdigit() for part in k.split('.')):
        c += 1
    else:
        d += 1

print('Số phần tử nguyên trong tập hợp A:', b)
print('Số phần tử số thực trong tập hợp A:', c)
print('Số phần tử là chuỗi kí tự trong tập hợp A:', d)
    
