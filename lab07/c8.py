A = set()
n = int(input("Nhập số lượng phần tử cho tập hợp A: "))
print("Nhập các phần tử cho tập hợp A: ")
for i in range(n):
    a = input("Nhập ptu: ")
    a.add(a)
b = 0
c = 0
d = 0
for k in A:
    if k.isdigit():
        b += 1
    elif '.' in k and all(part.isdigit() for part in k.split(".")):
        c += 1
    else:
        d +=1
print("Số phần tử là số nguyên trong tập hợp A: ", b)
print("Số phần tử là số thực trong tập hợp A: ", c)
print("Số phần tử là số chuỗi kí tự trong tập hợp A: ", d)
