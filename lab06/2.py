n = int(input("Nhập số lượng phần tử của danh sách: "))
a = []
b = []
print("Nhập các số tự nhiên:")
for i in range(n):
    num = int(input())
    a.append(num)
c = max(a)
for i, num in enumerate(a):
    if num < c:
        b.append(num)
max = max(b)
max_index = a.index(max)
print("Phần tử lớn thứ hai của danh sách là:", max)
print("Vị trí của phần tử lớn thứ hai là:", max_index)



n = int(input("Nhập số lượng phần tử của danh sách: "))
a = []
for i in range(n):
    num = int(input("Nhập phần tử thứ {}: ".format(i + 1)))
    a.append(num)
max_b = 0
c = 0
for num in a:
    if num > 0:
        c += 1
        if c > max_b:
            max_b = c
    else:
        c = 0
print("Số lượng các số dương liên tiếp nhiều nhất là:", max_b)



n = int(input("Nhập số lượng phần tử của danh sách: "))
a = []
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i + 1}: "))
    a.append(num)
max = 0
b = 0
c = 0
for num in a:
    if num > 0:
        b += num
        c += 1
    else:
        if b > max:
            max = b
            k = c
        b = 0
        c = 0
if b > max:
    max = b
    k = c
print("Số lượng các số dương liên tiếp có tổng lớn nhất là:", k)



