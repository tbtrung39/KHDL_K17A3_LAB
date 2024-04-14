n = int(input("Nhập số phần tử của danh sách: "))
while n <= 0:
    n = int(input("Số phần tử của danh sách phải lớn hơn 0, vui lòng nhập lại: "))
danh_sach = []
for i in range(n):
    phan_tu = int(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach.append(phan_tu)
print("Danh sách các số tự nhiên nhập vào là:", danh_sach)
#Tìm phần tử lớn thứ hai của danh sách và vị trí của phần tử đó
sap_xep = sorted(danh_sach, reverse= True)
phan_tu_lon_thu_hai = sap_xep[1]
print("Phần tử lớn thứ hai của danh sách là:",phan_tu_lon_thu_hai)
vi_tri = danh_sach.index(phan_tu_lon_thu_hai)
print("Vị trí của phần tử",phan_tu_lon_thu_hai,"là:",vi_tri)
#Tìm số lượng các số dương liên tiếp nhiều nhất
max = 0
so_luong = 0
for i in danh_sach:
    if i>0:
        so_luong +=1
    else:
        if so_luong > max:
            max = so_luong
        so_luong = 0
if so_luong > max:
    max = so_luong        
print("Số lượng các số dương liên tiếp nhiều nhất là:",max)   
#Tính số lượng các số dương liên tiếp có tổng lớn nhất 
tong_max = 0
so_luong_tong_max = 0
tong_ban_dau = 0
so_luong_ban_dau = 0
for i in danh_sach:
    if i > 0:
        tong_ban_dau += i
        so_luong_ban_dau += 1
    else:
        if tong_ban_dau > tong_max:
            tong_max = tong_ban_dau
            so_luong_tong_max = so_luong_ban_dau
        tong_ban_dau = 0
        so_luong_ban_dau = 0
if tong_ban_dau > tong_max:
    tong_max = tong_ban_dau
    so_luong_tong_max = so_luong_ban_dau        
print("Số lượng các số dương liên tiếp có tổng lớn nhất là:",so_luong_tong_max)                
                