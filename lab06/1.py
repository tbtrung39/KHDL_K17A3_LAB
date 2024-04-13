a= [2, -4, 1, 9, -3, 6, 3, -2, 6, 8] 
tong_cac_phan_tu=sum(a)
print("Tổng các phần tử của danh sách là: ", tong_cac_phan_tu)

so_phan_tu_duong=[x for x in a if x > 0] 
so_luong_phan_tu_duong=len(so_phan_tu_duong)
tong_cac_phan_tu_duong=sum(so_phan_tu_duong)
print("Số lượng số hạng dương là: ", so_luong_phan_tu_duong)
print("Tổng các số hạng dương là: ", tong_cac_phan_tu_duong)
vi_tri_am_dau_tien= None
for i in range(len(a)):
    if a[i]<0:
        vi_tri_am_dau_tien=i
        break
print ("Vị trí của phần tử âm đầu tiên là: ", vi_tri_am_dau_tien)
vi_tri_duong_cuoi_cung=None
for i in range(len(a) -1, -1, -1):
    if a[i] > 0:
        vi_tri_duong_cuoi_cung = i
        break
print("Vị trí của phần tử dương cuối cùng là: ", vi_tri_duong_cuoi_cung)
phan_tu_lon_nhat=max(a)
vi_tri_phan_tu_lon_nhat_cuoi_cung=len(a) -1 -a[:: -1]. index(phan_tu_lon_nhat)
print ("Phần tử lớn nhất của danh sách:", phan_tu_lon_nhat)
print ("Vị trí của phần tử lớn nhất cuối cùng:", vi_tri_phan_tu_lon_nhat_cuoi_cung)