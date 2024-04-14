a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
b = []
tong = 0
for i in a:
    tong += i
print("Tổng các phần tử trong danh sách là: ", tong)
# 
tong_duong = 0
for i in a:
    if i >0:
        b.append(i)
        tong_duong += i
print("Số lượng các phần tử dương trong danh sách là: ", len(b))
print("Tổng các phần tử dương trong danh sách là: ", tong_duong)
# 
for i in range(len(a)):
    if a[i] < 0:
        print("Vị trí phần tử âm đầu tiên là: ", i)
        break
# 
for i in range(len(a) -1, -1, -1):
    if a[i] > 0:
        print("Vị trí của phần tử duơng cuối cùng là: ", i)
        break
#
phan_tu_max = a[0]
for i in a:
    if i > phan_tu_max:
        phan_tu_max = i
        vi_tri = a.index(phan_tu_max)
print("Phần tử lớn nhất là: ", phan_tu_max)
print("Vị trí của phần tử lớn nhất là: ", vi_tri)
