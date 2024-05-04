def tim_max_min(a,b,c):
    max_3_so = max(a,b,c)
    min_3_so = min(a,b,c)
    return max_3_so , min_3_so

a = int(input('Nhập vào số thứ nhất: '))
b = int(input('Nhập vào số thứ hai: '))
c = int(input('Nhập vào số thứ ba: '))
max_3_so, min_3_so = tim_max_min(a,b,c)
print(f'Số nhỏ nhất là: {min_3_so}')
print(f'Số lớn nhất là: {max_3_so}')