a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
print(f"Tổng phần tử của danh sách là :{sum(a)}")


b=[]
sum_a=0
for i in a:
    if i > 0:
        b.append(i)
        sum_a += i
        break
print(f"Có {len(b)} số hạng  dương.")      
print(f"Tổng các số hạng dương là:{sum_a}")

vi_tri=-1
for i in range(len(a)):
    if a[i] < 0:
        vi_tri = i
        break
print(f"Vị trí phần tử âm đầu tiên của danh sách là: {vi_tri}")

vi_tri_1=-1
for i in range(len(a)):
    if a[i] > 0:
        vi_tri_1 = i
        break
print(f"Vị trí phần tử dương đầu tiên của danh sách là: {vi_tri_1}")

print(f"Phần tử lớn nhất danh sách là: {max(a)} ")
print(f"Vị trí phần tử lớn nhất danh sách là : {a.index(max(a))}")