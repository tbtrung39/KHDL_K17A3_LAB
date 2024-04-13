a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
dem = 0
for i in a:
    dem += i
print("Tổng các phần tử trong danh sách bằng:", dem)


a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
Dem = 0
Tong = 0
for i in a:
    if i > 0:
        Dem += 1
        Tong += i
print("Số lượng các số hạng dương là:", Dem)
print("Tổng của các số hạng dương bằng:", Tong)


a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
b = None
for i, c in enumerate(a):
    if c < 0:
        b = i
        break
if b is not None:
    print("Vị trí của phần tử âm đầu tiên là:", b)
else:
    print("Không có vị trí của phần tử âm đầu tiên")


a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
b = None
for i in range(len(a) -1, -1, -1):
    if a[i] > 0:
        b = i
        break
if b is not None:
    print("Vị trí của phần tử dương cuối cùng là:", b)
else:
    print("Không có vị trí của phần tử dương cuối cùng")


a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
max = None
c = None
for i, so in enumerate(a):
    if max is None or so >= max:
        max = so
        c = i
if c is not None:
    print("Phần tử lớn nhất của danh sách là:", max)   
    print("Vị trí phần tử lớn nhất cuối cùng là:", c) 
else:
    print("Danh sách rỗng")    




