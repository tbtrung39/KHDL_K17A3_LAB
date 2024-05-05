chieu_cao = [161, 182, 161, 154, 176, 171, 150, 167, 142, 179, 178, 163, 162, 165, 165, 155, 153, 175]
#cau a
so_luong = len(chieu_cao)
print(f"Nhom co {so_luong} sinh vien")
#cau b
tong = sum(chieu_cao)
chieu_cao_trung_binh = tong/so_luong
print(f"Chieu cao trung binh cac sinh vien trong nhom la: {chieu_cao_trung_binh} ")
#cau c
unique_cc = set(chieu_cao)
s = sum(chieu_cao)
sx = sorted(unique_cc)
sl = len(chieu_cao)
chieu_cao_trung_binh = s/sl
print("Cac chieu cao khac nhau: ")
for chieu_cao in sx:
    print(chieu_cao)
print(f"Chieu cao trung binh la: {chieu_cao_trung_binh}")    
