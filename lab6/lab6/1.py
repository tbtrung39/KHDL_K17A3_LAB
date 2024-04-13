a=[2,-4,1,9,-3,6,3,-2,6,8]
print(f'tong cac phan tu cua danh sach là: {sum(a)}')
d=0
tong=0
for i in a:
    if i>0:
        d+=1
        tong+=i
print(f'so luong cac so hang duong {d}, tong cua cac so hang duong {tong}')
for i in range(len(a)):
    if a[i]<0:
        print(f'vị trí phan tu âm đầu tiên trong danh sách là: {i}')
        break
for i in range(len(a)-1,-1,-1):
    if a[i]>0:
        print(f'vị trí của phân tử cuối cùng của danh sách là {i}')
        break

vtln= len(a)-a[::-1].index(max(a))
print(f'phần tử lớn nhất của danh sách {a[vtln-1]} và vị trí lớn nhất cuối cùng là {vtln-1}')