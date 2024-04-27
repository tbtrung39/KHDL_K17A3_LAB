a = [2,-4,1,9,-3,6,3,-2,6,8]
# tính tổng phần tử trong list
tong = 0
for i in a:
    tong +=1
print("Tổng các phần tử của list là: ", tong)

# đếm số hạng dương và tính tổng của chúng
tong1 = 0
so_duong = 0
for i in a:
    if i >=0:
        tong1 +=i
        so_duong +=i
print("Số hạng dương của list là: ", so_duong, "và tổng số hạng dương là: ", tong1)

# vị trí phần tử âm đầu tiên
print(a[1], "là phần tử âm đầu tiên của list")

# vị trí phần tử dương cuối
print(a[-1], "là phần tử dương cuối của list")

# tìm phần tử max và vị trí của nó
b = str(a[3])
print(enumerate(b))