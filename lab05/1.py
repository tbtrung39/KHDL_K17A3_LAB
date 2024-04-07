# cho danh sách a=[2,-4,1,9,-3,6,3,-2,6,8] gồm n=10 phần tử
# viết chương trình python tính tổng các phần tử của danh sách
a = [2,-4,1,9,-3,6,3,-2,6,8]
tong = 0
for i in a:
    tong+=i
print(tong)
# viết chương trình python đếm số lượng các số hạng dương và tổng của các số hạng dương
so_hang_duong = 0
tong1=0
for i in a:
    if i>0:
        so_hang_duong+=1
        tong1+=i
print(tong1)
# tìm vị trí của phần tử dương cuối cùng trong danh sách
for i in range (-1):
    if i>0:
        print(i,'là số dương cuối cùng')
        