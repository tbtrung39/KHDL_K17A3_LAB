danh_sach_chieu_cao = [
    161, 182, 161, 154, 176, 170, 167, 171,
    170, 174, 150, 142, 148, 165, 170, 178,
    156, 145, 149, 163, 162, 159, 165,
    165, 170, 180, 155, 159, 155, 153,
    152, 162, 180, 168, 169, 168, 167, 170
]

so_luong_hoc_sinh = len(danh_sach_chieu_cao)

tong_chieu_cao = sum(danh_sach_chieu_cao)

chieu_cao_trung_binh = tong_chieu_cao / so_luong_hoc_sinh

chieu_cao_khac_nhau = set(danh_sach_chieu_cao)

print(f"Có {so_luong_hoc_sinh} học sinh trong nhóm.")
print(f"Chiều cao trung bình của các học sinh trong nhóm là {chieu_cao_trung_binh:.2f} cm.")
print(f"Các chiều cao khác nhau của học sinh trong nhóm là: {sorted(list(chieu_cao_khac_nhau))}")
