a = [2,-4,1,9,-3,6,3,-2,6,8]
tong = 0 
for i in a:
    tong += i
print('tong cua list :',tong)

so_duong = 0
tong_so_duong = 0
for i in a:
    if i > 0:
        tong_so_duong += i
        so_duong +=1 
print('tong so duong :',tong_so_duong)
print('so_duong',so_duong)


i = 0
vi_tri = None
while i < len(a):
    if a[i] < 0:
        vi_tri = i
        break
    i += 1
if vi_tri is not None:
    print('vi tri ', vi_tri)
else:
    print('Không tìm thấy số âm trong danh sách')