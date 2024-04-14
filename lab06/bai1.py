danh_sach = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
#Tính tổng các phần tử dương trong danh sách
tong = sum(danh_sach)
print("Tổng của danh sách a là:",tong)
#Đếm số lượng các số hạng dương
so_luong_phan_tu_duong = 0
for i in (danh_sach):
    if i > 0:
        so_luong_phan_tu_duong+=1
print("Số lượng các số hạng dương có trong danh sách là:",so_luong_phan_tu_duong)
#Tính tổng của các số hạng dương
phan_tu_duong = []
for j in (danh_sach):
    if j >0:
        phan_tu_duong.append(j)
        tong_pt_duong = sum(phan_tu_duong)
print("Tổng các phần tử dương có trong danh sách là:",tong_pt_duong)        
#Tìm vị trí của phần tử âm đầu tiên trong danh sách
vi_tri_am_dau_tien = None
for i in range(len(danh_sach)):
    if danh_sach[i] <0:
        vi_tri_am_dau_tien = i
        break
if vi_tri_am_dau_tien !=None:
    print("Vị trí phần tử âm đầu tiên trong danh sách là:",vi_tri_am_dau_tien)
else:
    print("Không có phần tử âm trong danh sách")
#Tìm vị trí của phần tử dương cuối cùng trong danh sách   
vi_tri_duong_cuoi_cung = None
for i in range (len(danh_sach) -1, -1, -1):
    if danh_sach[i] >0:
        vi_tri_duong_cuoi_cung = i
        break
if vi_tri_duong_cuoi_cung != None:
    print("Vị trí phần tử dương cuối cùng trong danh sách là:",vi_tri_duong_cuoi_cung)
else:
    print("Không có phần tử dương trong danh sách")  
#Phần tử lớn nhất trong danh sách
phan_tu_max = max(danh_sach)
print("Phần tử lớn nhất của danh sách là:",phan_tu_max)
#Vị trí của phần tử lớn nhất
vi_tri = danh_sach.index(phan_tu_max)
print("Vị trí của phần tử lớn nhất trong danh sách là:",vi_tri)          