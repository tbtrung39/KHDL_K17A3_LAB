chieu_cao_sinh_vien=[161, 182, 161, 154, 176, 171, 170, 174, 150, 142, 165, 170, 178, 156, 145, 149, 163, 162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170 ]
so_luong_sinh_vien=len(chieu_cao_sinh_vien)
chieu_cao_trung_binh=sum(chieu_cao_sinh_vien)/(so_luong_sinh_vien)
print("Nhóm có tổng cộng số lượng sinh viên:", so_luong_sinh_vien)
print("Chiều cao trung bình của các sinh viên trong nhóm:", chieu_cao_trung_binh)
thong_ke_chieu_cao={ }
for chieu_cao in chieu_cao_sinh_vien:
    thong_ke_chieu_cao[chieu_cao]=thong_ke_chieu_cao.get(chieu_cao, 0)+1
tong_chieu_cao=sum(thong_ke_chieu_cao)
so_luong_chieu_cao_khac_nhau=len(chieu_cao_sinh_vien)
chieu_cao_trung_binh=tong_chieu_cao/len(chieu_cao_sinh_vien)
for chieu_cao in thong_ke_chieu_cao:
    print(chieu_cao)
print("Chiều cao trung bình của nhóm là: ", chieu_cao_trung_binh)
