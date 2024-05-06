n=int(input('nhập số lượng của danh sách: '))
ds=[int(input(f'nhập phần tử thứ {i+1}: ')) for i in range(n)]
print(ds)
a=filter(lambda x: x%2!=0,ds)
b=map(lambda x: x**2,a)
print('Danh sách chứa bình phương các số lẻ trong danh sách trên là: ',list(b))