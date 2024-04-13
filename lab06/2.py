so_luong_phan_tu=int(input("Nhập số phần tử của danh sách: "))
danh_sach=[]
for i in range(so_luong_phan_tu):
    phan_tu=int(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach.append(phan_tu)
lon_nhat=max(danh_sach)
danh_sach_khac_lon_nhat=[x for x in danh_sach if x != lon_nhat]
lon_thu_hai=max(danh_sach_khac_lon_nhat,default=None)
vi_tri_lon_thu_hai=danh_sach.index(lon_thu_hai) if lon_thu_hai is not None else None
print("Phần tử lớn thứ hai của danh sách:", lon_thu_hai)
print("Vị trí của phần tử lớn thứ hai:", vi_tri_lon_thu_hai)