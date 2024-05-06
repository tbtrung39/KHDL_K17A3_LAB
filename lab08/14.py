n = int(input('nhập số lượng danh sách: '))
A=[int(input(f'nhập phần tử thứ {i+1} (số nguyên): ')) for i in range(n)]
B=list(map(lambda x: x**2,A))
print(f'bình phương của các số hạng của danh sách {A} là: {B}')