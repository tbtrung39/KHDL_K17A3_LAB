chieu_cao = [161,182,175,173,153,190,182,188,192,140,176,177,150,184,189,180,170,165]

so_luong = len(chieu_cao)
print(f'Nhóm có {so_luong} sinh viên.')

tong = sum(chieu_cao)
chieu_cao_tb=tong/so_luong
print(f'Chiều cao trung bình của các sinh viên trong nhóm là: {chieu_cao_tb}')

unique_cc = set(chieu_cao)
s = sum(chieu_cao)
sx = sorted(unique_cc)
sl = len(chieu_cao)
cctb = s/sl 
print('Các chiều cao khác nhau: ')
for cc in sx:
    print(cc)
print(f'Chiều cao trung bình là: {cctb}')