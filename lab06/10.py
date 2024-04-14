a=[2,-4,1,9,-3,6,3,-2,6,8]
#
n=0
for i in a:
    n+=i
print(f"Tổng các phần tử: {n}")

#
m=0
k=0
for j in a:
    if j>0:
        k+=1
        m+=j
print("Số phần tử dương trong list là:",k)
print("Tổng các phần tử dương: ",m)


# Tìm vị trí của phần tử âm đầu tiên
vi_tri_am_dau = None
for i, x in enumerate(a):
 if x < 0:
    vi_tri_am_dau = i
    break
if vi_tri_am_dau is not None:
    print("Vị trí của phần tử âm đầu tiên:", vi_tri_am_dau)
else:
    print("Không có phần tử âm trong danh sách")


# Tìm phần tử lớn nhất và vị trí phần tử lớn nhất cuối cùng
max_value = max(a)
max_index = len(a) - 1 - a[::-1].index(max_value)
print("Phần tử lớn nhất:", max_value)
print("Vị trí của phần tử lớn nhất cuối cùng:", max_index)