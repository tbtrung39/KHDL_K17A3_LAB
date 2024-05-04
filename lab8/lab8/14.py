n = int(input('Nhập số lượng phần tử của danh sách: '))

print('Nhập các phần tử của danh sách:')
lst = list(map(int, input().split()))

list_binh_phuong = list(map(lambda x: x**2, lst))
print(f'Danh sách chứa bình phương của các phần tử là: {list_binh_phuong}')